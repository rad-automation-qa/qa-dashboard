import streamlit as st
import base64
import os


def create_docs_page():
    pdf_files = []

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    DESTINATION_DOCUMNETS_FOLDER = os.path.join(
        BASE_DIR, 'static', 'docs')

    # Check if the directory exists before trying to list files
    if os.path.exists(DESTINATION_DOCUMNETS_FOLDER):
        # Get a list of all PDF files in the folder
        pdf_files = [f for f in os.listdir(
            DESTINATION_DOCUMNETS_FOLDER) if f.endswith('.pdf')]
        print(f"PDF files found: {pdf_files}")
    else:
        print(f"Error: Folder {DESTINATION_DOCUMNETS_FOLDER} does not exist.")

    options = ["None"] + pdf_files

    # Create two columns
    col1, col2 = st.columns([1, 4])

    # Sidebar: List of PDF names (col1)
    with col1:
        st.write("### Available PDFs")
        selected_pdf = st.radio("Select a PDF:", options, index=0)

    # Display selected PDF in col2
    with col2:
        if selected_pdf != "None":
            pdf_path = os.path.join(DESTINATION_DOCUMNETS_FOLDER, selected_pdf)
            with open(pdf_path, "rb") as pdf_file:
                base64_pdf = base64.b64encode(pdf_file.read()).decode("utf-8")

            pdf_display = f'''
            <style>
            .pdf-container {{
                height: 90vh;
                position: relative;
            }}
            .pdf-container iframe {{
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
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
