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
from flask import Flask, render_template, make_response, request, redirect, url_for

# ? MongoDB --> For storing URL databases
from pymongo import MongoClient

# ? DateTime --> For getting current date
from datetime import datetime

# ? HashIDS --> For hashing URLs
from hashids import Hashids

# ? DotENV --> For storing keys
from dotenv import load_dotenv

# ? OS --> For getting .env file
from os import environ

# ? Random, String --> Last resort fail safe.
from random import choice as randchoice
from string import ascii_letters, digits, punctuation

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
print("Successfully connected MongoDB.")
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
            hashids = Hashids(
                min_length=10,
                salt=environ.get("KEY"),
                alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
            )
            id = usersColl.count_documents({}) + 1
            userID = hashids.encode(id)
            usersColl.insert_one({"ID": id, "UserID": userID})
            output = render_template(
                "signup.html", userID=userID, buttonVisible="buttoninvis"
            )
            resp = make_response(output)
            resp.set_cookie("userID", userID)
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
                resp.set_cookie("userID", userID)
                return resp
            else:
                return render_template("login.html", ErrorValid="errorTrue")
        else:
            return render_template("login.html")
    else:
        return redirect("/stats")


@app.route("/", methods=["GET", "POST"])
def home():
    if usersColl.find_one({"UserID": request.cookies.get("userID")}) != None:
        return redirect("/stats")
    else:
        return render_template("index.html")


@app.route("/generateurl", methods=["GET", "POST"])
def generateurl():
    global hasUsedApp
    if usersColl.find_one({"UserID": request.cookies.get("userID")}) != None:
        if request.method == "POST" and hasUsedApp == False:
            url = request.form["long_url"]
            if " " in url:
                print("INVALID URL")  # Aaloke add error - URL cannot have spaces in it.
                # return something
            elif "trim.lol" in url or "bit.ly" in url or "tinyurl.com" in url:
                print(
                    "INVALID URL"
                )  # Aaloke add another error - URL cannot be shortened.
                # return something
            customURL = request.form["custom_url"]
            now = datetime.now()
            id = URLsColl.count_documents({}) + 1
            time = now.strftime("%d/%m/%Y %H:%M:%S")
            userID = request.cookies.get("userID")
            if url == "":
                return render_template("generateurl.html", error_url="errorTrue")
            elif customURL != "":
                existingURLs = []
                for document in URLsColl.find({}, {"ShortenedURL": 1}):
                    existingURLs.append(document["ShortenedURL"])
                if customURL in existingURLs:
                    return render_template(
                        "generateurl.html", old_url=url, error_custom_url="errorTrue"
                    )
                elif (
                    " " in customURL
                    or any(char in punctuation for char in customURL)
                    or "www" in customURL
                    or "http" in customURL
                ):
                    print(
                        "CustomURL has space/punctuation"
                    )  # Aaloke same here - Invalid custom URL.
                    # return something
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
                )  # Aaloke - add some line to grey out all boxes, and remove shortenURL button.
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
                )  # Aaloke - add some line to grey out all boxes, and remove shortenURL button.
        elif request.method == "POST" and hasUsedApp == True:
            return redirect(url_for("generateurl"))
        else:
            hasUsedApp = False
            return render_template("generateurl.html", clearForms="True")
    else:
        return redirect("/")


@app.route("/stats", methods=["GET", "POST"])
def stats():
    if usersColl.find_one({"UserID": request.cookies.get("userID")}) != None:
        userID = request.cookies.get("userID")
        urls = list(URLsColl.find({"UserID": userID}, {"_id": 0}))
        if request.method == "POST":
            return render_template("stats.html", urls=urls)
        return render_template("stats.html", urls=urls)
    else:
        return redirect("/")


@app.route("/<id>")
def url_redirection(id):
    info = URLsColl.find_one({"ShortenedURL": id})
    if info:
        url = info["OriginalURL"]
        URLsColl.update_one({"ShortenedURL": id}, {"$inc": {"Clicks": 1}})
        return redirect(url)
    else:
        return redirect("/404")


@app.route("/404")
def error_404():
    return render_template("404.html")


# endregion
