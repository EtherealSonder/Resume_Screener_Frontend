import streamlit as st
from job_logic import create_job
from resume_logic import view_candidates, upload_and_score

st.set_page_config(page_title="Resume Screener Dashboard", layout="centered")
st.title("AI Resume Screener")

menu = st.sidebar.selectbox("Menu", ["View Candidates", "Create Job", "Upload Resume"])

if menu == "View Candidates":
    view_candidates()
elif menu == "Create Job":
    create_job()
elif menu == "Upload Resume": 
    upload_and_score()