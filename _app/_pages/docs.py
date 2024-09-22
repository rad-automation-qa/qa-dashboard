import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import os


def create_docs_page():
    pdf_files = []

    # Define the base directory and destination folder for PDF files
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    DESTINATION_DOCUMNETS_FOLDER = os.path.join(BASE_DIR, 'static', 'docs')

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

    # Sidebar: List of PDF document names (col1)
    with col1:
        st.write("### Available PDF Documents")
        selected_pdf = st.radio("Select a PDF Document:", options, index=0)

    # Display the selected PDF in col2 using streamlit-pdf-viewer
    with col2:
        if selected_pdf != "None":
            pdf_path = os.path.join(DESTINATION_DOCUMNETS_FOLDER, selected_pdf)
            # Load and display the selected PDF using streamlit_pdf_viewer
            with open(pdf_path, "rb") as pdf_file:
                binary_data = pdf_file.read()
                pdf_viewer(input=binary_data, width=1000)
        else:
            st.write("Please select a PDF document from the list.")


# Run the page
# create_docs_page()
