# 📝 Notes API — FastAPI + SQLAlchemy

A backend Notes API built using **FastAPI** and **SQLAlchemy**, focused on learning **real backend engineering fundamentals**: database integration, relationships, CRUD APIs, testing, and clean project structure.

This project follows a structured learning roadmap and currently represents **Week 2 (Backend Foundation — SQL + CRUD)**.

---

## 🚀 Features

* Create users
* Create, read, update, and delete notes
* Notes are linked to users using **foreign keys**
* Database-generated IDs (no in-memory counters)
* Clear separation of:

  * routes
  * database configuration
  * ORM models
  * request/response schemas
* Proper HTTP status codes and error handling
* Basic API tests using Pytest

---

## 🧠 Tech Stack

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **SQLite** (local development database)
* **Pydantic v2**
* **Pytest**
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
│   └── routes.py     # API routes
│
├── tests/
│   └── test_notes.py
│
├── conftest.py
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

## 🔌 API Endpoints

### Users

| Method | Endpoint | Description   |
| ------ | -------- | ------------- |
| POST   | `/users` | Create a user |

---

### Notes

| Method | Endpoint           | Description      |
| ------ | ------------------ | ---------------- |
| POST   | `/notes`           | Create a note    |
| GET    | `/notes/{note_id}` | Get a note by ID |
| PUT    | `/notes/{note_id}` | Update a note    |
| DELETE | `/notes/{note_id}` | Delete a note    |

---

## 📌 Example Request — Create Note

```json
{
  "user_id": 1,
  "title": "My first note",
  "content": "Learning FastAPI with SQLAlchemy"
}
```

### Example Response

```json
{
  "id": 1,
  "title": "My first note",
  "content": "Learning FastAPI with SQLAlchemy"
}
```

---

## 🧪 Testing

Run tests using:

```bash
pytest
```

Tests use FastAPI’s **in-memory HTTP client**, so no server needs to be running.

---

## 📈 Learning Goals Covered

* SQLAlchemy ORM fundamentals
* Database sessions and lifecycle
* Foreign keys and relational integrity
* CRUD API design
* Request vs response schemas
* Backend project structuring
* Git & GitHub workflow
* API testing with Pytest

---

## 📜 Notes

* SQLite is used for local development
* Password hashing and authentication are **not implemented yet**
* Authentication (JWT) will be added in the next phase

---

## 📜 License

This project is for learning and practice purposes.