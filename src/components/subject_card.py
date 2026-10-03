import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background: #1e1e2e; border-left: 8px solid #EB459E; padding: 25px; border-radius: 20px; border: 1px solid #313244; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);">
        <h3 style="margin: 0; color: #f5e0dc; font-size: 1.5rem;">{name}</h3>
        <p style="color: #a6adc8; margin: 10px 0;">Code : <span style="background: #313244; color: #94e2d5; padding: 2px 8px; border-radius: 5px; font-weight: 500;">{code}</span> | Section : <span style="color: #cdd6f4;">{section}</span></p>
        """

    if stats:
        html += """
        <div style="display:flex; gap:8px; flex-wrap:wrap; margin-top: 12px;">
        """
        for icon, label, value in stats:
            html += f'<div style="background: rgba(235, 69, 158, 0.15); border: 1px solid rgba(235, 69, 158, 0.3); color: #f5c2e7; padding: 5px 12px; border-radius: 12px; font-size: 0.9rem;">{icon} <b style="color: #ffffff;">{value}</b> <span style="color: #bac2de;">{label}</span></div>'

        html += "</div>"

    html += "</div>"  # Closed outer div tag

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()