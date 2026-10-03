import streamlit as st

def render_footer():
    footer_html = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: #888888;
        text-align: center;
        padding: 10px 0;
        font-size: 14px;
        z-index: 999;
    }
    .footer a {
        color: #0A66C2;
        text-decoration: none;
        font-weight: bold;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    
    <div class="footer">
        Created by <a href="www.linkedin.com/in/sahil-pasalkar"target="_blank">Sahil Pasalkar</a>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)