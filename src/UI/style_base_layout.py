import streamlit as st


def style_base_layout():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

        /* 1. App Background */
        .stApp {
            background-color: #222629 !important;
            font-family: 'Inter', sans-serif !important;
        }

        /* 2. Hide standard chrome */
        #MainMenu, footer, header {
            visibility: hidden;
        }

        .block-container {
            padding-top: 1.5rem !important;
        }

        /* 3. Typography */
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

        h3, h4 {
            color: #F2F2F2 !important;
            font-weight: 600 !important;
        }

        p, div, label, span {
            color: #F2F2F2 !important;
        }

        /* 4. Interactive Buttons with Smooth Glow & Lift Hover */
        div.stButton > button {
            background-color: #86C232 !important;
            color: #222629 !important;
            font-weight: 700 !important;
            border: 1px solid transparent !important;
            border-radius: 8px !important;
            padding: 0.6rem 1.25rem !important;
            transition: all 0.25s ease-in-out !important;
            cursor: pointer !important;
        }

        /* Hover State: Subtle Lift, Color Shift, and Accent Glow */
        div.stButton > button:hover {
            background-color: #61892F !important;
            color: #FFFFFF !important;
            border-color: #86C232 !important;
            transform: translateY(-3px) !important;
            box-shadow: 0px 8px 20px rgba(134, 194, 50, 0.35) !important;
        }

        /* Active Click State */
        div.stButton > button:active {
            transform: translateY(-1px) !important;
            box-shadow: 0px 4px 10px rgba(134, 194, 50, 0.2) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_dashboard():
    style_base_layout()


def style_background_home():
    st.markdown("""
       <style>
            st.App{
              background:# !important;

            }
            .stApp div[data-testid="stColumn"]{
                 Background-color:# !important;
                 padding:1.5rem !important;
                 border-radius:5rem
            }    
       </style>
    """)