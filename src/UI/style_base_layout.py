import streamlit as st


def style_base_layout():
    st.markdown(
        """
        <style>

        /* =========================================
           COMMON APP THEME
           ========================================= */

        /* App Background */
        .stApp {
            background-color: #222629 !important;
            font-family: 'Inter', sans-serif !important;
        }

        /* Import Font */
        @import url(
            'https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap'
        );

        /* =========================================
           HIDE STREAMLIT DEFAULT UI
           ========================================= */

        #MainMenu,footer,header {
            visibility: hidden;
        }

        .block-container {
            padding-top: 1.5rem !important;
        }

        /* =========================================
           TEXT
           ========================================= */

        h1 {
            color: #86C232 !important;
            font-size: 3rem !important;
            font-weight: 800 !important;
            margin-bottom: 0.5rem !important;
        }

        h2 {
            color: #61892F !important;
            font-size: 2rem !important;
            font-weight: 700 !important;
            margin-top: 1rem !important;
        }

        h3,
        h4 {
            color: #F2F2F2 !important;
            font-weight: 600 !important;
        }

        p,
        label,
        span {
            color: #F2F2F2 !important;
        }

        /* =========================================
           PRIMARY BUTTON
           ========================================= */

        div.stButton > button,
        div.stButton > button[data-testid="baseButton-primary"] {
            background-color: #86C232 !important;
            color: #222629 !important;
            font-weight: 700 !important;
            border: 1px solid transparent !important;
            border-radius: 8px !important;
            padding: 0.6rem 1.25rem !important;
            transition: all 0.25s ease-in-out !important;
            cursor: pointer !important;
        }

        div.stButton > button:hover,
        div.stButton > button[data-testid="baseButton-primary"]:hover {
            background-color: #61892F !important;
            color: #FFFFFF !important;
            border-color: #86C232 !important;
            transform: translateY(-3px) !important;
            box-shadow: 0px 8px 20px rgba(134, 194, 50, 0.35) !important;
        }

        div.stButton > button:active,
        div.stButton > button[data-testid="baseButton-primary"]:active {
            transform: translateY(-1px) !important;
            box-shadow: 0px 4px 10px rgba(134, 194, 50, 0.2) !important;
        }

        /* =========================================
           SECONDARY BUTTON
           ========================================= */

        div.stButton > button[data-testid="baseButton-secondary"] {
            background-color: #4E653E !important;
            color: #FFFFFF !important;
            font-weight: 700 !important;
            border: 1px solid #61892F !important;
            border-radius: 8px !important;
            padding: 0.6rem 1.25rem !important;
            transition: all 0.25s ease-in-out !important;
            cursor: pointer !important;
        }

        div.stButton > button[data-testid="baseButton-secondary"]:hover {
            background-color: #61892F !important;
            color: #FFFFFF !important;
            border-color: #86C232 !important;
            transform: translateY(-3px) !important;
            box-shadow: 0px 8px 20px rgba(97, 137, 47, 0.4) !important;
        }

        div.stButton > button[data-testid="baseButton-secondary"]:active {
            transform: translateY(-1px) !important;
            box-shadow: 0px 4px 10px rgba(97, 137, 47, 0.2) !important;
        }

        /* =========================================
           INPUTS
           ========================================= */

        input,
        textarea {
            background-color: #2F3336 !important;
            color: #FFFFFF !important;
            border: 1px solid #61892F !important;
        }

        /* =========================================
           SELECTBOX
           ========================================= */

        div[data-baseweb="select"] > div {
            background-color: #2F3336 !important;
            color: #FFFFFF !important;
            border-color: #61892F !important;
        }

        /* =========================================
           DASHBOARD COLUMNS / CARDS
           ========================================= */

        div[data-testid="stColumn"] {
            background-color: #222629 !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_dashboard():
    """
    Common background for Student and Teacher dashboards.
    """
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #222629 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_home():
    """
    Common background for the home/login page.
    """
    st.markdown(
        """
        <style>

        .stApp {
            background-color: #222629 !important;
        }

        div[data-testid="stColumn"] {
            background-color: #222629 !important;
            padding: 1.5rem !important;
            border-radius: 1rem !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    ) 