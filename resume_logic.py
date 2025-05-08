import streamlit as st
import pandas as pd
from db import get_connection
import requests

def upload_and_score():
    st.header("Upload Resume for Scoring")
    

    job_title = st.selectbox("Job Title", [
    "Frontend Developer",
    "Full Stack Developer",
    "Machine Learning Engineer",
    "DevOps Engineer",
    "AI Research Intern",
    "Game Designer",
    "Unity Technical Artist",
    "Unreal Engine Developer",
    "Cloud Engineer (AWS/GCP)",
    "Mobile App Developer",
    "Computer Vision Engineer",
    "NLP Engineer",
    "QA Automation Engineer",
    "Business Intelligence Analyst",
    "Web Developer"
])

    resume_file = st.file_uploader("Upload Resume (PDF)")
    cover_letter = st.text_area("Optional Cover Letter", height=200)


    if st.button("Evaluate") and resume_file and job_title:
        with st.spinner("Evaluating..."):
            response = requests.post(
                "http://localhost:5000/parse_resume",
                files={"resume": resume_file},
                data={"job_title": job_title, "cover_letter": cover_letter}
            )
            print("API response:", response.status_code, response.text)

            if response.status_code == 200:
                result = response.json()
                st.success(f"Score: {result['score']}")
                st.write(result["summary"])
                st.write("**Strengths:**", result["strengths"])
                st.write("**Weaknesses:**", result["weaknesses"])
            else:
                st.error("Evaluation failed.")

def view_candidates():
    st.header("Top Candidates")

    with get_connection() as conn:
        df = pd.read_sql("""
            SELECT j.job_title, r.candidate_name, r.email, r.score, r.summary
            FROM resumes r
            JOIN jobs j ON r.job_id = j.id
            ORDER BY r.score DESC
            LIMIT 10
        """, conn)

    st.dataframe(df)

    if not df.empty:
        st.subheader("Score Distribution")
        st.bar_chart(df["score"])