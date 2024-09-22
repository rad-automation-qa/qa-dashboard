import streamlit as st
import base64
import os

from constants import DESTINATION_DOCUMNETS_FOLDER


def create_docs_page():
    folder_path = DESTINATION_DOCUMNETS_FOLDER

    # Get a list of all PDF files in the folder
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    # Add a placeholder option at the beginning
    options = ["None"] + pdf_files

    # Create two columns
    col1, col2 = st.columns([1, 4])

    # Sidebar: List of PDF names (col1)
    with col1:
        st.write("### Available PDFs")
        # "None" is pre-selected
        selected_pdf = st.radio("Select a PDF:", options, index=0)

    # Display selected PDF in col2
    with col2:
        if selected_pdf != "None":
            pdf_path = os.path.join(folder_path, selected_pdf)
            with open(pdf_path, "rb") as pdf_file:
                base64_pdf = base64.b64encode(pdf_file.read()).decode("utf-8")
            # Display the PDF in an iframe with custom CSS
            pdf_display = f'''
            <style>
            .pdf-container {{
                height: 90vh; /* Adjust based on your needs */
                position: relative;
            }}
            .pdf-container iframe {{
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 97%;
                border: none;
            }}
            </style>
            <div class="pdf-container">
                <iframe src="data:application/pdf;base64,{base64_pdf}" type="application/pdf"></iframe>
            </div>
            '''
            st.markdown(pdf_display, unsafe_allow_html=True)
        else:
            st.write("Please select a PDF from the list.")
