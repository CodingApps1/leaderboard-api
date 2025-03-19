# 🏆 Leaderboard Application (Full Stack - React + Flask)

![React](https://img.shields.io/badge/React-18-blue)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-red)

## 🚀 Overview
This is a **full-stack leaderboard application** that allows users to **view, add, and delete users and manage scores dynamically**. It consists of:

1. **Frontend (React + Vite)**
2. **Backend (Flask + SQLAlchemy API)**

This file **includes API endpoints documentation only**.

## 📢 **This repo leverages Leaderboard FrontEnd React Repository repository for Frontend Services**

### 📢 **The documentation to setup this repo is provided in the readme of  https://github.com/CodingApps1/leaderboard-frontend-react.git**
🔗 **Leaderboard FrontEnd React Repository:** https://github.com/CodingApps1/leaderboard-frontend-react.git

---

# 📡 Leaderboard API Documentation

## 📌 Base URL: http://127.0.0.1:5000/api
## 🏆 **Leaderboard Endpoints**


```json

Get All Users
Endpoint: /users>
Method: GET
Description: Fetches all users and their leaderboard scores.
Response:
[
  {
    "id": 1,
    "name": "Emma",
    "age": 25,
    "points": 30,
    "address": "123 Street"
  },
  {
    "id": 2,
    "name": "Noah",
    "age": 28,
    "points": 20,
    "address": "456 Avenue"
  }
]

Get a Single User
Endpoint: /users/<id>
Method: GET
Description: Fetch details of a single user by ID.
Example Request: /users/1
Response:
{
  "id": 1,
  "name": "Emma",
  "age": 25,
  "points": 30,
  "address": "123 Street"
}


Add a New User
Endpoint: /users
Method: POST
Description: Adds a new user to the leaderboard.
Request Body:
{
  "name": "Liam",
  "age": 22,
  "points": 0,
  "address": "789 Boulevard"
}
Response:
{
  "message": "User added successfully",
  "user": {
    "id": 3,
    "name": "Liam",
    "age": 22,
    "points": 0,
    "address": "789 Boulevard"
  }
}

Update User Points
Endpoint: /users/<id>
Method: PUT
Description: Updates a user's points in the leaderboard.
Example Request: /users/1
Request Body:
{
  "points": 35
}
Response:
{
  "message": "User updated successfully",
  "user": {
    "id": 1,
    "name": "Emma",
    "age": 25,
    "points": 35,
    "address": "123 Street"
  }
}

Delete a User
Endpoint: /users/<id>
Method: DELETE
Description: Removes a user from the leaderboard.
Example Request: /users/3
Response:
{
  "message": "User deleted successfully"
}


