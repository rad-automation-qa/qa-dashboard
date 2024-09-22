import shutil
import os

from constants import SOURCE_DOCUMNETS_FOLDER, DESTINATION_DOCUMNETS_FOLDER


def copy_pdf_docs(src_folder, dest_folder):
    try:
        # Check if the destination folder exists, if not, create it
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        # Loop through all the files in the source folder
        for file_name in os.listdir(src_folder):
            # Check if the file is a PDF
            if file_name.endswith(".pdf"):
                # Construct full file path
                src_file_path = os.path.join(src_folder, file_name)
                dest_file_path = os.path.join(dest_folder, file_name)

                # Copy the file to the destination folder
                shutil.copy(src_file_path, dest_file_path)
                print(f"Copied: {file_name} to {dest_folder}")
    except Exception as e:
        print(e)


copy_pdf_docs(SOURCE_DOCUMNETS_FOLDER, DESTINATION_DOCUMNETS_FOLDER)
