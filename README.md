# URL Shortener

## About the Project
URLShortener is a robust and user-friendly solution designed to simplify the management and sharing of long web addresses. With its intuitive interface and efficient backend powered by Flask and MongoDB, this project offers a seamless experience for shortening URLs. Developed with a focus on practicality and ease of use, URLShortener provides users with a reliable ally in managing their online links effortlessly.

## Purpose
The purpose of this project is to learn how to deal with databases, web development frameworks, and various libraries used in creating a URL shortener. This project provides hands-on experience with technologies like MongoDB, Flask, and Tailwind CSS.

## Live Preview
Check out the live preview of the website [here](http://example.com).

This website is currently hosted at [trim.lol](https://trim.lol).

## Setting Up Locally

### Prerequisites
Make sure you have Python and MongoDB installed on your system.

- **[Python](https://www.python.org/downloads/)**: Download and install Python.
- **[MongoDB](https://docs.mongodb.com/manual/installation/)**: Follow the installation guide for MongoDB.
- **[MongoDB Compass](https://www.mongodb.com/products/compass)**: Download and install MongoDB Compass for a GUI to interact with MongoDB.

### Installation Steps

1. **Clone the repository**
    ```bash
    git clone https://github.com/AverageBlank/URLShortener.git
    cd URLShortener
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On bash use `source venv/bin/activate`
    ```

3. **Install the required libraries**
    ```bash
    pip install flask pymongo datetime hashids python-dotenv
    ```

4. **Set up environment variables**
    - Create a `.env` file in the root directory of the project.
    - Add your MongoDB URI and a secret key in the `.env` file. For example:
        ```env
        link={your_mongodb_uri}
        SECRET_KEY={your_secret_key}
        ```

5. **Run MongoDB**
    - Start the MongoDB server. If you installed MongoDB locally, you can start it with the following command:
        ```bash
        mongod
        ```

6. **Connect to MongoDB with MongoDB Compass**
    - Open MongoDB Compass.
    - In the "New Connection" window, enter your MongoDB URI in the connection string field (this is the same URI you put in the `.env` file).
    - Click "Connect" to connect to your MongoDB server.
    - You can now view and manage your databases and collections through the Compass GUI.

7. **Run the application**
    ```bash
    flask --app app run
    ```

8. **Open your browser**
    - Navigate to `http://127.0.0.1:5000/` to see the application running locally.

## Languages Used
- **Python**: The main programming language used for the backend.
- **HTML**: Markup language used for structuring the web pages.
- **Tailwind CSS**: A utility-first CSS framework for styling the web pages.
- **JavaScript**: Programming language used for client-side scripting.

## Libraries Used
- **Flask**: A lightweight WSGI web application framework in Python.
    ```bash
    pip install flask
    ```
- **PyMongo**: A Python distribution containing tools for working with MongoDB.
    ```bash
    pip install pymongo
    ```
- **Datetime**: A module to work with dates and times.
    ```bash
    pip install DateTime
    ```
- **Hashids**: A small library to generate YouTube-like hashes from one or many numbers.
    ```bash
    pip install hashids
    ```
- **Python-dotenv**: Reads key-value pairs from a `.env` file and can set them as environment variables.
    ```bash
    pip install python-dotenv
    ```
- **OS**: A standard library in Python to interact with the operating system. (Built-in, no need to install)
- **Random**: Implements pseudo-random number generators for various distributions. (Built-in, no need to install)
- **String**: A built-in Python library to perform common string operations. (Built-in, no need to install)
