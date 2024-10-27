# Starting of the program
#! --------------------------------------------------
#! ---------- Credits
#! --------------------------------------------------
# region credits
# * ---- Made by:
# * ------- Aaloke Eppalapalli
# * ------- Husain Khorakiwala

# * ---- Source Code:
# * ------- https://github.com/AverageBlank/URLShortener
# endregion


#! --------------------------------------------------
#! ---------- Imports
#! --------------------------------------------------
# region import
# ? Flask --> For the backend of HTML
import os
import certifi
from flask import (
    Flask,
    render_template,
    make_response,
    request,
    redirect,
    url_for,
    session
)


# ? MongoDB --> For storing URL databases
from pymongo import MongoClient

# ? DateTime --> For getting current date
from datetime import datetime, timedelta

# ? HashIDS --> For hashing URLs
from hashids import Hashids

# ? DotENV --> For storing keys
from dotenv import load_dotenv

# ? OS --> For getting .env file
from os import environ

# ? Random, String --> Last resort fail safe.
from random import choice as randchoice
from string import ascii_letters, digits, punctuation

# ? Requests --> For making requests
from flask import Flask, render_template , redirect, flash ,url_for, session, request, jsonify
#from flask_oauthlib.client import OAuth
from authlib.integrations.flask_client import OAuth
import requests

# endregion
#! --------------------------------------------------
#! --------------------------------------------------


#! --------------------------------------------------
#! ---------- Running the Program
#! --------------------------------------------------
# region Running the Program
# ? Required.
app = Flask(__name__)
app.config["SECRET_KEY"] = environ.get("SECRET_KEY")
domain = "https://trim.lol/"
hasUsedApp = False


# ? Google OAuth Client ID, Secret, and Redirect URI
google_client_id = os.environ.get('google_client_id')
google_client_secret = os.environ.get('google_client_secret')
google_redirect_uri = os.environ.get('google_redirect_uri')

# ? Setting OAuth App
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=google_client_id,
    client_secret=google_client_secret,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url = 'https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'email profile'
    },
    
)
# ? Connecting to the Mongo DB Database
load_dotenv()
mongoLink = environ.get("link")
client = MongoClient(mongoLink)
db = client["URLShorteners"]

# ? Connecting to Collections
URLsColl = db["urls"]
usersColl = db["users"]

# ? Create indexes (if needed)
URLsColl.create_index("ID", unique=True)
URLsColl.create_index("Timestamp")
URLsColl.create_index("OriginalURL")
URLsColl.create_index("ShortenedURL", unique=True)
URLsColl.create_index("Clicks")
URLsColl.create_index("UserID")

usersColl.create_index("ID", unique=True)
usersColl.create_index("UserID", unique=True)
print("Successfully connected to MongoDB.")
# endregion
#! --------------------------------------------------
#! --------------------------------------------------


#! --------------------------------------------------
#! ---------- Functions
#! --------------------------------------------------
# region Functions
@app.route("/signup", methods=("GET", "POST"))
def signUp():
    global userID
    if usersColl.find_one({"UserID": request.cookies.get("userID")}) == None:
        if request.method == "POST":
            load_dotenv()
            id = usersColl.count_documents({}) + 1
            users = usersColl.distinct("UserID")
            while True:
                key = ""
                for _ in range(10):
                    key += randchoice(ascii_letters + digits)
                hashids = Hashids(
                    min_length=10,
                    salt=key,
                    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
                )
                userID = hashids.encode(id)
                if userID in users:
                    continue
                break
            usersColl.insert_one({"ID": id, "UserID": userID})
            output = render_template(
                "signup.html", userID=userID, buttonVisible="buttoninvis"
            )
            resp = make_response(output)
            expiration_date = datetime.now() + timedelta(days=30)
            expiration_timestamp = expiration_date.timestamp()
            resp.set_cookie("userID", userID, expires=expiration_timestamp)
            return resp
        else:
            return render_template("signup.html", userID="Your User ID")
    else:
        return redirect("/stats")


@app.route("/login", methods=["GET", "POST"])
def logIn():
    global userID
    if usersColl.find_one({"UserID": request.cookies.get("userID")}) == None:
        if request.method == "POST":
            userID = request.form["userid"]
            userPresent = usersColl.find_one({"UserID": userID})
            if userPresent:
                output = redirect("/stats")
                resp = make_response(output)
                expiration_date = datetime.now() + timedelta(days=30)
                expiration_timestamp = expiration_date.timestamp()
                resp.set_cookie("userID", userID, expires=expiration_timestamp)
                return resp
            else:
                return render_template("login.html", ErrorValid="errorTrue")
        else:
            return render_template("login.html")
    else:
        return redirect("/stats")

# login for google
@app.route('/login/google')
def login_google():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize_google', _external=True)
    return google.authorize_redirect(redirect_uri)
    
# authorize for google
@app.route('/authorize/google')
def authorize_google():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    
    userID = user_info.get('email')
    
    # Check if user already exists, if not, insert into usersColl
    if not usersColl.find_one({"UserID": userID}):
        new_user_id = usersColl.count_documents({}) + 1
        usersColl.insert_one({"ID": new_user_id, "UserID": userID})
    
    # Save user ID in cookies and redirect to /stats
    response = make_response(redirect("/stats"))
    expiration_date = datetime.now() + timedelta(days=30)
    response.set_cookie("userID", userID, expires=expiration_date.timestamp())
    return response
    

@app.route("/", methods=["GET", "POST"])
def home():
    if usersColl.find_one({"UserID": request.cookies.get("userID")}) != None:
        return redirect("/stats")
    else:
        response = make_response(render_template("index.html"))
        if request.cookies.get("userID") != None:
            response.set_cookie("userID", "", expires=0)
        return response

@app.route("/generateurl", methods=["GET", "POST"])
def generateurl():
    global hasUsedApp
    if usersColl.find_one({"UserID": request.cookies.get("userID")}) != None:
        if request.method == "POST" and hasUsedApp == False:
            customURL = ""
            url = request.form["long_url"]
            customURL = request.form["custom_url"]
            if " " in url:
                if customURL == "":
                    return render_template(
                        "generateurl.html",
                        error_url="errorTrue",
                        error_url_statement="Invalid URL. Please try again.",
                    )
                else:
                    return render_template(
                        "generateurl.html",
                        error_url="errorTrue",
                        custom_url=customURL,
                        error_url_statement="Invalid URL. Please try again.",
                    )
            elif "trim.lol" in url or "bit.ly" in url or "tinyurl.com" in url:
                if customURL == "":
                    return render_template(
                        "generateurl.html",
                        error_url="errorTrue",
                        error_url_statement="URL cannot be shortened. Please try again.",
                    )
                else:
                    return render_template(
                        "generateurl.html",
                        error_url="errorTrue",
                        custom_url=customURL,
                        error_url_statement="URL cannot be shortened. Please try again.",
                    )
            now = datetime.now()
            id = URLsColl.count_documents({}) + 1
            time = now.strftime("%d/%m/%Y %H:%M:%S")
            userID = request.cookies.get("userID")
            if url == "":
                return render_template(
                    "generateurl.html",
                    error_url="errorTrue",
                    error_url_statement="Please enter a URL and try again.",
                )
            elif customURL != "":
                existingURLs = []
                for document in URLsColl.find({}, {"ShortenedURL": 1}):
                    existingURLs.append(document["ShortenedURL"])
                if customURL in existingURLs:
                    return render_template(
                        "generateurl.html",
                        old_url=url,
                        error_custom_url="errorTrue",
                        error_custom_url_statement="Custom URL already claimed. Please try again.",
                    )
                elif (
                    " " in customURL
                    or any(char in punctuation for char in customURL)
                    or "www" in customURL
                    or "http" in customURL
                ):
                    return render_template(
                        "generateurl.html",
                        old_url=url,
                        error_custom_url="errorTrue",
                        error_custom_url_statement="Invalid custom URL. Please try again.",
                    )
                else:
                    URLsColl.insert_one(
                        {
                            "ID": id,
                            "Timestamp": time,
                            "OriginalURL": url,
                            "ShortenedURL": customURL,
                            "Clicks": 0,
                            "UserID": userID,
                        }
                    )
                    hasUsedApp = True
                    return render_template(
                        "generateurl.html",
                        old_url=url,
                        new_url=domain + customURL,
                        custom_url=customURL,
                        completed="True",
                    )
            else:
                hashid = Hashids(min_length=5, salt=userID)
                newURL = hashid.encode(id)
                existingURLs = []
                for document in URLsColl.find({}, {"ShortenedURL": 1}):
                    existingURLs.append(document["ShortenedURL"])
                while newURL in existingURLs:
                    salt = ""
                    for _ in range(10):
                        salt += randchoice(ascii_letters + digits)
                    hashid = Hashids(
                        min_length=7,
                        salt=salt,
                    )
                    newURL = hashid.encode(id)
                URLsColl.insert_one(
                    {
                        "ID": id,
                        "Timestamp": time,
                        "OriginalURL": url,
                        "ShortenedURL": newURL,
                        "Clicks": 0,
                        "UserID": userID,
                    }
                )
                hasUsedApp = True
                return render_template(
                    "generateurl.html",
                    old_url=url,
                    new_url=domain + newURL,
                    custom_url=" ",
                    completed="True",
                )
        elif request.method == "POST" and hasUsedApp == True:
            hasUsedApp = False
            return redirect(url_for("generateurl"))
        else:
            hasUsedApp = False
            return render_template("generateurl.html", clearForms="True")
    else:
        response = make_response(redirect("/"))
        if request.cookies.get("userID") != None:
            response.set_cookie("userID", "", expires=0)
        return response


@app.route("/stats", methods=["GET", "POST"])
def stats():
    userID = request.cookies.get("userID")
    print("UserID in /stats:", userID)  # Debugging output
    if userID and usersColl.find_one({"UserID": userID}) != None:
        urls = list(URLsColl.find({"UserID": userID}, {"_id": 0}))
        return render_template("stats.html", urls=urls, userID=userID)
    else:
        response = make_response(redirect("/"))
        response.set_cookie("userID", "", expires=0)
        return response


@app.route("/<id>")
@app.route("/<id>/")
def url_redirection(id):
    info = URLsColl.find_one({"ShortenedURL": id})
    if info:
        url = info["OriginalURL"]
        URLsColl.update_one({"ShortenedURL": id}, {"$inc": {"Clicks": 1}})
        return redirect(url)
    else:
        return redirect("/404")


@app.route("/logout")
def logout():
    response = make_response(redirect("/"))
    response.set_cookie("userID", "", expires=0, path="/", max_age=0)
    return response


@app.route("/404")
def error_404():
    return render_template("404.html")


# endregion

if __name__ == "__main__":
    app.run(debug=True)
