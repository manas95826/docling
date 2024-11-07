# Document to Markdown Converter

This Streamlit app allows users to upload a document file (PDF, DOCX, or TXT), convert it to Markdown format, view the result, and download the Markdown file.

## Features

- **Upload Documents**: Users can upload PDF, DOCX, or TXT files.
- **Convert to Markdown**: The uploaded document is converted into Markdown format using `docling`.
- **Downloadable Output**: The converted Markdown text can be downloaded as a file.

## Installation

1. Clone this repository (or download the code).
2. Install the necessary dependencies:

   ```bash
   pip install streamlit docling
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run doc-to-md.py
   ```

2. Open the link provided in the terminal (typically `http://localhost:8501`) to access the app in your web browser.

3. **Upload Document**: Use the "Upload Document" button to upload a PDF, DOCX, or TXT file.
4. **View Markdown**: Once uploaded, the app will display the converted Markdown text.
5. **Download Markdown File**: Click on "Download Markdown File" to download the Markdown text as a `.md` file.

## Project Structure

- `app.py`: Main Streamlit app file.
- `requirements.txt`: List of required Python packages for easy installation (optional).

## Example Workflow

1. Upload a document (e.g., `sample.pdf`).
2. The app converts the content to Markdown and displays it.
3. Download the result by clicking the "Download Markdown File" button.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [Docling](https://pypi.org/project/docling/)

## License

This project is licensed under the MIT License.

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.
