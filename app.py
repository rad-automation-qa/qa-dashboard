import os
import streamlit as st

from _app._pages.projects import create_projects_page
from _app._pages.docs import create_docs_page
from _app._pages.system_tools import create_system_page
from _app.data import rad_logo


def set_title(title):
    st.markdown(
        f"""
            <div style='text-align: center; color: grey; font-size: 3em; font-weight: bold; margin-top: -50px;'>{title}</div>
        """,
        unsafe_allow_html=True
    )

    st.divider()


if __name__ == "__main__":
    st.set_page_config(layout="wide",
                       page_icon=rad_logo)

    st.sidebar.image(rad_logo, use_column_width=True)
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Select a page", ["Projects", "System Tools", "Documents"])

    set_title(page)

    if page == "Projects":
        create_projects_page()
    elif page == "System Tools":
        create_system_page()
    elif page == "Documents":
        create_docs_page()
