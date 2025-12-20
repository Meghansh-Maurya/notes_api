# 📝 Notes API — FastAPI + SQLAlchemy + JWT

A backend Notes API built using **FastAPI** and **SQLAlchemy**, focused on learning **real backend engineering fundamentals**: authentication, authorization, database relationships, and secure CRUD APIs.

This project follows a structured learning roadmap and currently represents **Week 2 (Backend Foundation — SQL, Auth, Secure CRUD)**.

---

## 🚀 Features

* User signup and login
* JWT-based authentication
* Create, read, update, and delete notes
* Notes are strictly scoped to the authenticated user
* Secure ownership enforcement (users cannot access others’ notes)
* Database-generated IDs (no in-memory counters)
* Clear separation of:

  * routes
  * database configuration
  * ORM models
  * request/response schemas
* Proper HTTP status codes and error handling

---

## 🧠 Tech Stack

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **SQLite** (local development database)
* **Pydantic v2**
* **JWT (JSON Web Tokens)**
* **Uvicorn**

---

## 📁 Project Structure

```
notes_application/
│
├── app/
│   ├── __init__.py
│   ├── main.py        # FastAPI app entry point
│   ├── database.py   # DB engine + session handling
│   ├── models.py     # SQLAlchemy models + Pydantic schemas
│   ├── routes.py     # API routes
│   └── security.py   # Password hashing + JWT utilities
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Activate virtual environment

```bash
# Windows
env\Scripts\activate

# macOS / Linux
source env/bin/activate
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the server

```bash
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

### 4️⃣ Open API Docs

Visit:

```
http://127.0.0.1:8000/docs
```

Use Swagger UI or Postman to test endpoints.

---

## 🔐 Authentication Flow

1. **Signup** → create user
2. **Login** → receive JWT access token
3. **Send token** as `Authorization: Bearer <token>`
4. Access protected note endpoints

JWT is required for all note-related operations.

---

## 🔌 API Endpoints

### Authentication

| Method | Endpoint  | Description       |
| ------ | --------- | ----------------- |
| POST   | `/signup` | Create a new user |
| POST   | `/login`  | Login and get JWT |

---

### Notes (JWT Protected)

| Method | Endpoint           | Description      |
| ------ | ------------------ | ---------------- |
| POST   | `/notes`           | Create a note    |
| GET    | `/notes/{note_id}` | Get a note by ID |
| PUT    | `/notes/{note_id}` | Update a note    |
| DELETE | `/notes/{note_id}` | Delete a note    |

---

## 📌 Example — Create Note

### Request (JWT required)

```json
{
  "title": "My first note",
  "content": "Learning FastAPI with SQLAlchemy and JWT"
}
```

### Response

```json
{
  "id": 1,
  "title": "My first note",
  "content": "Learning FastAPI with SQLAlchemy and JWT"
}
```

> **Note:**
> The client never sends `user_id`.
> Ownership is derived from the authenticated JWT token.

---

## 🔒 Security Highlights

* Passwords are hashed before storage
* JWT tokens are signed and verified
* User identity is never trusted from client input
* Notes are accessible only by their owner
* Unauthorized access returns `404` to avoid data leakage

---

## 📈 Learning Goals Covered

* SQLAlchemy ORM fundamentals
* Database sessions and lifecycle
* Foreign keys and relational integrity
* JWT authentication and verification
* Authorization and ownership enforcement
* Secure CRUD API design
* Backend project structuring
* Git & GitHub workflow

---

## 📜 Notes

* SQLite is used for local development
* This project prioritizes **correct backend design over shortcuts**
* Frontend integration and CORS will be added in the next phase

---

## 📜 License

This project is for learning and practice purposes.


