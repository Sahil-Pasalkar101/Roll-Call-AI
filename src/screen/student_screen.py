import streamlit as st

def student_screen():
    st.header("Welcome to the Student Portal!")
    st.write("This is the student dashboard.")

    # Button to log out / return to home screen
    if st.button("Log Out / Back to Home"):
        st.session_state["login_type"] = None
        st.rerun()
 
