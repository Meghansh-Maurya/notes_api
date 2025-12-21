# 📝 Notes App — FastAPI + Streamlit

A full-stack Notes application built with **FastAPI (backend)** and **Streamlit (frontend)**, focused on learning **real backend engineering concepts**: authentication, authorization, database relationships, and client–server interaction.

This project was built step-by-step as part of a structured learning roadmap and currently represents Frontend Integration.

---

## 🚀 Features

### 🔐 Authentication

* User signup
* Login with JWT (Bearer token)
* Secure password hashing
* Token-based authentication

### 🗒 Notes Management

* Create notes
* View all notes (user-scoped)
* Edit notes
* Delete notes
* Notes are strictly **owned by users** (authorization enforced on backend)

### 🖥 Frontend

* Built using Streamlit
* Login & signup UI
* Create, edit, delete notes from UI
* JWT stored in client session state
* UI reacts to auth state (login/logout)

---

## 🧠 Tech Stack

### Backend

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **SQLite**
* **Pydantic v2**
* **JWT (OAuth2PasswordBearer)**
* **Uvicorn**

### Frontend

* **Streamlit**
* **Requests**

---

## 📁 Project Structure

```
notes_application/
│
├── app/
│   ├── __init__.py
│   ├── main.py        # FastAPI app entry point
│   ├── database.py   # DB engine & session handling
│   ├── models.py     # SQLAlchemy models + Pydantic schemas
│   ├── routes.py     # Auth & Notes API routes
│   └── security.py   # Password hashing & JWT logic
│
├── frontend.py       # Streamlit frontend
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

### 3️⃣ Run the backend (FastAPI)

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### 4️⃣ Run the frontend (Streamlit)

Open a new terminal (same env):

```bash
streamlit run frontend.py
```

Frontend runs at:

```
http://localhost:8501
```

---

## 🔌 API Endpoints (Backend)

### Auth

| Method | Endpoint  | Description     |
| ------ | --------- | --------------- |
| POST   | `/signup` | Create new user |
| POST   | `/login`  | Login & get JWT |

### Notes (JWT required)

| Method | Endpoint      | Description        |
| ------ | ------------- | ------------------ |
| GET    | `/notes`      | Get all user notes |
| GET    | `/notes/{id}` | Get single note    |
| POST   | `/notes`      | Create note        |
| PUT    | `/notes/{id}` | Update note        |
| DELETE | `/notes/{id}` | Delete note        |

---

## 🔐 Security Design (Important)

* Frontend **never sends `user_id`**
* Backend derives user identity from JWT
* All note operations are scoped using:

  ```
  note.user_id == current_user.id
  ```
* Prevents unauthorized access and ID tampering (BOLA protection)

---

## 🧠 Key Concepts Learned

* JWT-based authentication & authorization
* Password hashing & verification
* SQLAlchemy ORM & relationships
* Backend ownership enforcement
* Client–server separation
* Streamlit reactive UI model
* Session-based frontend state
* Secure CRUD design

---

## 📌 Notes

* SQLite is used for local development
* CORS & deployment will be added next
* This project prioritizes **understanding over shortcuts**

---

## 📜 License

This project is for learning and practice purposes.

