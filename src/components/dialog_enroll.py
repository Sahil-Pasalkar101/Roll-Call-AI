
import streamlit as st
import time

from src.database.db import enroll_student_to_subject
from src.database.config import supabase


@st.dialog("Enroll in Subject")
def enroll_dialog():
    st.write("Enter the subject code provided by your teacher to enroll")

    join_code = st.text_input(
        "Subject Code",
        placeholder="Eg. CS101"
    )

    if st.button(
        "Enroll now",
        type="primary",
        width="stretch"
    ):

        # Check if subject code is empty
        if not join_code:
            st.warning("Please enter a subject code")
            return

        # Clean the subject code
        join_code = join_code.strip().upper()

        try:
            # Find the subject
            res = (
                supabase
                .table("subjects")
                .select("subject_id, name, subject_code")
                .eq("subject_code", join_code)
                .execute()
            )

            # Subject does not exist
            if not res.data:
                st.error(
                    "Invalid subject code. Please check the code and try again."
                )
                return

            # Get subject
            subject = res.data[0]

            # Get logged-in student
            student_id = st.session_state.student_data["student_id"]

            # Check if already enrolled
            check = (
                supabase
                .table("subject_students")
                .select("*")
                .eq("subject_id", subject["subject_id"])
                .eq("student_id", student_id)
                .execute()
            )

            if check.data:
                st.warning(
                    "You are already enrolled in this subject."
                )
                return

            # Enroll student
            result = enroll_student_to_subject(
                student_id,
                subject["subject_id"]
            )

            # Check result
            if result:
                st.success(
                    f"Successfully enrolled in {subject['name']}!"
                )
                time.sleep(1)
                st.rerun()
            else:
                st.error(
                    "Enrollment failed. Please try again."
                )

        except Exception as e:
            st.error(
                "Something went wrong while enrolling."
            )
            st.code(str(e))

