<p align="center">
   <a href="https://github.com/StarPandaBeg/CodeCat">
    <img src=".github/logo.png" alt="Logo" width="128" />
   </a>

   <h3 align="center">CodeCat - CodeForces problem storage</h3>

   <p align="center">
      Simple problem & solution storage for codeforces, leetcode, etc.
   </p>
</p>

---

<p align="center">
  <img src=".github/gui.png">
</p>

This is a simple pet project created for learning Flask and organizing personal achievements. Designed to be fast and lightweight, it allows users to store problems from platforms like Codeforces, attach solutions with explanations, and search problems by its text.

# Features

- **Task Organization**: Problems can be organized by attaching them to competitions.
- **Full-text Search**: Enables searching tasks by their text content.
- **Solution Attachment**: Users can attach solutions with explanations to problems for better understanding and reference.

# Getting started

0. In any chosen installation way, you need to set FLASK_SECRET_KEY environment variable to some unique string. 

   You can do this, for example, by creating `.env` file from example:
   ```
   FLASK_SECRET_KEY="018fef43f3697937b4b7357502ebe21b"

   DATABASE_URL="sqlite:///.data/database.db"
   ```
   > ⚠ Keep your secret key in private. Do not use value from above!

## Docker Compose Support

1. You can install this app from container

   ```
   $ docker compose up
   ```

## Manual

1. Ensure you have Python 3.10 installed
   ```
   $ python --version
   Python 3.10.8
   ```
1. Install dependencies
   ```
   $ pip install -r requirements.txt
   ```
1. Run app

   ```
   $ flask run
   ```

   > ⚠ Ensure you have set the secret key on step 0.


Open your web browser and visit `http://localhost:15356`. You should see a basic app page.

# License

Distributed under the MIT License.  
See `LICENSE` for more information.

# Disclaimer

This project is my first Flask application. It may contain errors or inaccuracies. I would appreciate your feedback and suggestions for improvement. Thanks! 💗