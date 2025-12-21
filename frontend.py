import streamlit as st
import requests

try:
    API_BASE_URL = st.secrets["API_BASE_URL"]
except FileNotFoundError:
    API_BASE_URL = "http://127.0.0.1:8000"
except KeyError:
    API_BASE_URL = "http://127.0.0.1:8000"

st.title("Notes App")

if "token" not in st.session_state:
    st.session_state.token = None

if "selected_note" not in st.session_state:
    st.session_state.selected_note = None


if not st.session_state.token:
    st.subheader("Sign Up")
    signup_username = st.text_input("Username", key="signup_username")
    signup_password = st.text_input(
        "Password", key="signup_password", type="password")

    if st.button("Sign Up", key="signup_button"):
        response = requests.post(
            f"{API_BASE_URL}/signup",
            json={
                "username": signup_username,
                "password": signup_password
            }
        )

        if response.status_code == 200:
            st.success("User created successfully. Please log in.")

        else:
            st.error(f"Error {response.status_code}: {response.text}")


    st.subheader("Login")

    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input(
        "Password", key="login_password", type="password")

    if st.button("Login", key="login_button"):
        response = requests.post(
            f"{API_BASE_URL}/login",
            json={
                "username": login_username,
                "password": login_password
            }
        )

        if response.status_code == 200:
            st.session_state.token = response.json()["access_token"]
            st.success("Logged in successfully")
            st.rerun()
        else:
            st.error("Invalid credentials")


if st.session_state.token:
    st.subheader("My Notes")

    headers = {
        "Authorization": f"Bearer {st.session_state.token}"
    }

    response = requests.get(
        f"{API_BASE_URL}/notes",
        headers=headers
    )

    if response.status_code == 200:
        notes = response.json()

        if not notes:
            st.info("No notes yet")
        else:
            for note in notes:
                if st.button(note["title"], key=f"note_{note['id']}"):
                    st.session_state.selected_note = note
                    st.rerun()

                st.write(note["content"])
                if st.button("Delete", key = f"delete_{note['id']}"):
                    note_id = note["id"]
                    del_response = requests.delete(
                        f"{API_BASE_URL}/notes/{note_id}",
                        headers=headers
                    )
                    st.rerun()
                st.divider()
    else:
        st.error("Failed to fetch notes")


if st.session_state.token:
    st.subheader("Create Note")

    title = st.text_input("Title", key="note_title")
    content = st.text_area("Content", key="note_content")

    if st.button("Create Note"):
        headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

        response = requests.post(
            f"{API_BASE_URL}/notes",
            headers=headers,
            json={
                "title": title,
                "content": content
            }
        )

        if response.status_code == 200:
            st.success("Note created")
            st.rerun()
        else:
            st.error("Failed to create note")

    if st.button("Logout", key="logout", type = "primary"):
        st.session_state.token = None
        st.rerun()


if st.session_state.selected_note:
    st.subheader("Edit Note")

    edited_title = st.text_input(
        "Title",
        value=st.session_state.selected_note["title"]
    )

    edited_content = st.text_area(
        "Content",
        value=st.session_state.selected_note["content"]
    )

    if st.button("Update Note"):
        headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

        note_id = st.session_state.selected_note["id"]

        response = requests.put(
            f"{API_BASE_URL}/notes/{note_id}",
            headers=headers,
            json={
                "title": edited_title,
                "content": edited_content
            }
        )

        if response.status_code == 200:
            st.success("Note updated")
            st.session_state.selected_note = None
            st.rerun()
        else:
            st.error("Failed to update note")
