# 🔗 trim.lol - URL Shortener

## Overview

URLShortener is a robust, user-friendly application designed to make managing and sharing long web addresses simpler. Built with an efficient backend powered by Flask, and secure database provided by MongoDB, the tool provides a smooth experience for shortening long URLs. It is built with a focus on practicality, usability, and reliability, helping users manage their URL links with ease.

## Live Preview

https://github.com/AverageBlank/URLShortener/assets/112507212/f0203f19-f348-4267-953c-c99db8e5476d

This website is currently hosted at [trim.lol](https://trim.lol). Hosted using [Vercel](https://vercel.com/)

## Contribution

Please check out [CONTRIBUTION.md](https://github.com/AvgBlank/URLShortener/blob/Master/CONTRIBUTION.md) for more information regarding contribution.

## Setting up Locally using Docker (Recommended Method)

### Prerequisites

Ensure you have Docker installed on your system.

- **[Docker](https://www.docker.com/)**: Download and install Docker.

### Installation Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/AverageBlank/URLShortener.git
   cd URLShortener
   ```

2. **Setup environment variables**

- Create a `.env` file in the root directory of the project and paste the following variables:

  ```env
  link={your_mongo_uri}
  SECRET_KEY={your_secret_key}
  ```

  - Now set the `link` and `SECRET_KEY` variables in the `.env` file according to your needs.

3. **Run the container**

- Start the MongoDB & Flask server with one of the following command:
  ```bash
  docker compose up
  ```
  **_or if you encounter compatibility issues, use the following command:_**
  ```bash
  docker-compose up
  ```

4. **Open your browser**

   - Navigate to `http://127.0.0.1:5000/` to see the application running locally.

## Setting up Locally (without Docker)

### Prerequisites

Ensure you have **Python** and **MongoDB** installed on your system.

- **[Python](https://www.python.org/downloads/)**: Install Python.
- **[MongoDB](https://docs.mongodb.com/manual/installation/)**: Follow MongoDB's installation guide.
- **[MongoDB Compass](https://www.mongodb.com/products/compass)** **_(optional)_**: A GUI for MongoDB.

### Installation Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/AverageBlank/URLShortener.git
   cd URLShortener
   ```

2. **Run install script**

   - Linux/MacOS: `bash install.sh`
   - Windows: `.\install.bat`

3. **Run MongoDB**

   - Start the MongoDB server. If you installed MongoDB locally, you can start it with the following command:
     ```bash
     mongod
     ```

4. **Connect to MongoDB with MongoDB Compass** **_(optional)_**

   - Open MongoDB Compass.
   - In the "New Connection" window, enter your MongoDB URI in the connection string field (this is the same URI you entered during the install phase (present in the `.env` file in root directory of the project)).
   - Click "Connect" to connect to your MongoDB server.
   - You can now view and manage your databases and collections through the Compass GUI.

5. **Run the application**

   - Linux/MacOS: `bash start.sh`
   - Windows: `.\start.bat`

6. **Open your browser**
   - Navigate to `http://127.0.0.1:5000/` to see the application running locally.

## Tech Stack

- **[Python](https://www.python.org/)**: The main programming language used for the backend.
- **[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)**: Markup language used for structuring the web pages.
- **[Tailwind CSS](https://tailwindcss.com/)**: A utility-first CSS framework for styling the web pages.
- **[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)**: Programming language used for client-side scripting.

### Python Libraries Used

- **[Flask](https://flask.palletsprojects.com/)**: A lightweight WSGI web application framework in Python.
- **[PyMongo](https://pymongo.readthedocs.io/)**: A Python distribution containing tools for working with MongoDB.
- **[Datetime](https://docs.python.org/3/library/datetime.html)**: A module to work with dates and times.
- **[Hashids](https://hashids.org/python/)**: A small library to generate YouTube-like hashes from one or many numbers.
- **[Python-dotenv](https://saurabh-kumar.com/python-dotenv/)**: Reads key-value pairs from a `.env` file and can set them as environment variables.
- **[OS](https://docs.python.org/3/library/os.html)**: A standard library in Python to interact with the operating system. Built-in Python library
- **[Random](https://docs.python.org/3/library/random.html)**: Implements pseudo-random number generators for various distributions. Built-in Python library
- **[String](https://docs.python.org/3/library/string.html)**: A built-in Python library to perform common string operations.
- **[Gunicorn](https://gunicorn.org/)**: Python WSGI HTTP Server for UNIX systems(Used for Render Hosting. Ignore if running local instance)
