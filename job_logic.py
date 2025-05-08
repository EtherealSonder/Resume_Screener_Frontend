import streamlit as st
from db import get_connection

def create_job():
    st.header("Create New Job Posting")
    title = st.text_input("Job Title")
    description = st.text_area("Job Description")
    location = st.text_input("Location")

    if st.button("Submit Job"):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO jobs (job_title, job_description, location)
                    VALUES (%s, %s, %s)
                """, (title, description, location))
                conn.commit()
        st.success("Job created successfully!")