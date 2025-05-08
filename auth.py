import streamlit as st
import requests

API_URL = "http://localhost:5000/login"

# Session state for login tracking
if "client" not in st.session_state:
    st.session_state.client = None

def login():
    st.title("Client Login")
    email = st.text_input("Email")
    if st.button("Login"):
        response = requests.post(API_URL, json={"email": email})
        if response.status_code == 200:
            st.session_state.client = response.json()
            st.success(f"Welcome {st.session_state.client['name']}")
            st.rerun()

        else:
            st.error("Login failed. Try a valid email.")