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
   - In the "New Connection" window, enter your MongoDB URI in the connection string field (this is the same URI you enterd during the install phase (present in the `.env` file in rooe dir of the project)).
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
