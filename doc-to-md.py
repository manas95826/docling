import streamlit as st
from docling.document_converter import DocumentConverter
import tempfile
import os

def main():
    # App Title
    st.title("Document to Markdown Converter")
    st.write("Upload a document to get the Markdown text and download it.")

    # File Uploader
    uploaded_file = st.file_uploader("Upload Document", type=["pdf", "docx", "txt"])

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            file_path = tmp_file.name

        # Initialize DocumentConverter
        converter = DocumentConverter()
        
        # Convert Document
        try:
            result = converter.convert(file_path)
            markdown_text = result.document.export_to_markdown()

            # Display Markdown Output
            st.subheader("Converted Markdown")
            st.markdown(markdown_text)

            # Downloadable Markdown file
            markdown_filename = "converted_document.md"
            with open(markdown_filename, "w") as f:
                f.write(markdown_text)

            # Download Button
            with open(markdown_filename, "rb") as f:
                st.download_button(
                    label="Download Markdown File",
                    data=f,
                    file_name=markdown_filename,
                    mime="text/markdown"
                )
                
            # Clean up temporary file
            os.remove(file_path)

        except Exception as e:
            st.error(f"An error occurred during conversion: {e}")

if __name__ == "__main__":
    main()
