import streamlit as st

def teacher_screen():
    st.header("Welcome to the Teacher Portal!")
    st.write("This is the teacher dashboard.")

    # Button to log out / return to home screen
    if st.button("Log Out / Back to Home"):
        st.session_state["login_type"] = None
        st.rerun()
