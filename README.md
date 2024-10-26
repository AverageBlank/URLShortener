# URL Shortener

## About the Project

URLShortener is a robust and user-friendly solution designed to simplify the management and sharing of long web addresses. With its intuitive interface and efficient backend powered by Flask and MongoDB, this project offers a seamless experience for shortening URLs. Developed with a focus on practicality and ease of use, URLShortener provides users with a reliable ally in managing their online links effortlessly.

## Purpose

The purpose of this project is to learn how to deal with databases, web development frameworks, and various libraries used in creating a URL shortener. This project provides hands-on experience with technologies like MongoDB, Flask, and Tailwind CSS.

## Live Preview

https://github.com/AverageBlank/URLShortener/assets/112507212/f0203f19-f348-4267-953c-c99db8e5476d

<!-- This website is currently hosted at [trim.lol](https://trim.lol). -->
This website is not currently being hosted.

## Contribution
Please checkout [CONTRIBUTION.md](https://github.com/AvgBlank/URLShortener/blob/Master/CONTRIBUTION.md) for more information regarding contribution

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

2. **Run install script**

   For Linux
   ```bash
   bash install.sh
   ```

   For Windows
   ```bash
   ./install.bat
   ```

3. **Run MongoDB**

   - Start the MongoDB server. If you installed MongoDB locally, you can start it with the following command:
     ```bash
     mongod
     ```

4. **Connect to MongoDB with MongoDB Compass**

   - Open MongoDB Compass.
   - In the "New Connection" window, enter your MongoDB URI in the connection string field (this is the same URI you entered during the install phase (present in the `.env` file in root directory of the project)).
   - Click "Connect" to connect to your MongoDB server.
   - You can now view and manage your databases and collections through the Compass GUI.

5. **Run the application**

   For Linux
   ```bash
   bash start.sh
   ```

   For Windows
   ```bash
   ./start.bat
   ```

6. **Open your browser**
   - Navigate to `http://127.0.0.1:5000/` to see the application running locally.

## Setting Up Locally Using Docker

### Prerequisites

Make sure you have Docker installed on your system.

- **[Docker](https://www.docker.com/)**: Download and install Docker.

1. **Clone the repository**

   ```bash
   git clone https://github.com/AverageBlank/URLShortener.git
   cd URLShortener
   ```

2. **Setup environment variables**

   - Create a `.env` file in the root directory of the project and paste the following variables:
     ```env
      # Common credentials
      DB_USERNAME={your_mongodb_username}
      DB_PASSWORD={your_mongodb_password}
      SECRET_KEY={your_secret_key}
      DB_HOST=database
      DB_NAME=URLShorteners
      
      # Flask App
      link=mongodb://${DB_USERNAME}:${DB_PASSWORD}@${DB_HOST}/${DB_NAME}?authSource=admin&retryWrites=true&w=majority
      
      # MongoDB
      MONGO_INITDB_ROOT_USERNAME=${DB_USERNAME}
      MONGO_INITDB_ROOT_PASSWORD=${DB_PASSWORD}
      MONGO_INITDB_DATABASE=${DB_NAME}
     ```
   - Now set the DB_USERNAME, DB_PASSWORD & SECRET_KEY variables in the `.env` file according to your needs.

3. **Run the containers**

   - Start MongoDB & Flask server with the following command:
     ```bash
     docker compose up
     ```

4. **Open your browser**
   - Navigate to `http://127.0.0.1:5000/` to see the application running locally.

## Tech Stack

- **Python**: The main programming language used for the backend.
- **HTML**: Markup language used for structuring the web pages.
- **Tailwind CSS**: A utility-first CSS framework for styling the web pages.
- **JavaScript**: Programming language used for client-side scripting.

## Python Libraries Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **PyMongo**: A Python distribution containing tools for working with MongoDB.
- **Datetime**: A module to work with dates and times.
- **Hashids**: A small library to generate YouTube-like hashes from one or many numbers.
- **Python-dotenv**: Reads key-value pairs from a `.env` file and can set them as environment variables.
- **OS**: A standard library in Python to interact with the operating system. Built-in Python library
- **Random**: Implements pseudo-random number generators for various distributions. Built-in Python library
- **String**: A built-in Python library to perform common string operations.
- **Gunicorn**: Python WSGI HTTP Server for UNIX systems(Used for Render Hosting. Ignore if running local instance)
