import streamlit as st
from auth import login 
from job_logic import create_job
from resume_logic import view_candidates, upload_and_score

st.set_page_config(page_title="Resume Screener Dashboard", layout="centered")

if st.session_state.client is None:
    login()
    st.stop()
    

st.title(f"Resume Screener - {st.session_state.client['name']}")

menu = st.sidebar.selectbox("Menu", ["View Candidates", "Create Job", "Upload Resume"])

if menu == "View Candidates":
    view_candidates()
elif menu == "Create Job":
    create_job()
elif menu == "Upload Resume": 
    upload_and_score()