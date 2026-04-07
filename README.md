# 📝 Notes App — FastAPI + PostgreSQL + Streamlit

A **full-stack Notes application** built with **FastAPI**, **PostgreSQL**, and **Streamlit**, focused on learning **real backend engineering fundamentals** and deploying a working product end-to-end.

This project covers **authentication, database design, secure CRUD, deployment, and frontend integration**.

🔗 **Live App:** [https://notesapi.streamlit.app/](https://notesapi.streamlit.app/)   (currently disabled)

---

## 🚀 Features

### 🔐 Authentication

* User signup & login
* JWT-based authentication
* Secure password hashing
* Token-protected APIs

### 📝 Notes Management

* Create, read, update, delete notes
* Notes are **strictly user-owned**
* Users can only access their own data
* Database-generated IDs (no in-memory hacks)

### 🌐 Deployment

* Backend deployed on **Render**
* PostgreSQL running in production
* Frontend deployed on **Streamlit Cloud**
* CORS configured correctly for browser security

---

## 🧠 Tech Stack

### Backend

* **Python**
* **FastAPI**
* **SQLAlchemy ORM**
* **PostgreSQL**
* **Pydantic v2**
* **JWT (Authentication)**

### Frontend

* **Streamlit**
* **Requests (API calls)**

### Infrastructure

* **Render** (Backend + Database)
* **Streamlit Cloud** (Frontend)
* **GitHub** (Version control)

---

## 📁 Project Structure

```
notes_application/
│
├── app/
│   ├── __init__.py
│   ├── main.py       # FastAPI app entry point
│   ├── database.py   # DB engine + session handling
│   ├── models.py     # ORM models + Pydantic schemas
│   ├── routes.py     # Auth & Notes APIs
│   └── security.py   # Password hashing + JWT logic
│
├── frontend.py       # Streamlit frontend
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ▶️ Run Locally (Optional)

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

### 3️⃣ Set environment variables

```bash
DATABASE_URL=postgresql://...
SECRET_KEY=your_secret_key
```

---

### 4️⃣ Run backend

```bash
uvicorn app.main:app --reload
```

---

### 5️⃣ Run frontend

```bash
streamlit run frontend.py
```

---

## 🔌 API Overview

### Auth

* `POST /signup`
* `POST /login`

### Notes (JWT required)

* `POST /notes`
* `GET /notes`
* `GET /notes/{note_id}`
* `PUT /notes/{note_id}`
* `DELETE /notes/{note_id}`

---

## 🔐 Security Design (Important)

* Passwords are **hashed**, never stored in plain text
* JWT tokens are **signed using a server secret**
* User identity is derived from JWT, **not client input**
* All note operations enforce **user ownership**

---

## 📈 What This Project Teaches

* How CRUD works **in theory and reality**
* Why authentication must be server-controlled
* How JWT actually secures APIs
* How ORMs manage DB + in-memory state
* How deployments fail (and how to fix them)
* How frontend talks to a real backend
* Why CORS exists and how to configure it
* How to ship, not just code

---

## 🧭 Roadmap Status

* ✅ Backend foundation (FastAPI + SQLAlchemy)
* ✅ Authentication (JWT)
* ✅ PostgreSQL migration
* ✅ Production deployment
* ✅ Frontend integration
* 🔜 Testing (Pytest)
* 🔜 GenAI features (RAG, LLM APIs)

---

## 📜 License

This project is built for **learning, experimentation, and portfolio use**.

