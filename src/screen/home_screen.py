import streamlit as st
from src.components.Header import header_home
from src.UI.style_base_layout import style_base_layout,style_background_dashboard,style_background_home
def home_screen():
    header_home()
    style_base_layout()
    col1, col2 = st.columns(2)
    with col1:
        st.header("I'm Student")
        st.image("src\logos\Student_logo.png", width=120)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='student'
            st.rerun()

    with col2:
        st.header("I'm Teacher")
        st.image("src\logos\Teacher_logo.png", width=145)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='teacher'
            st.rerun()