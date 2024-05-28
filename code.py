import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pdf2image import convert_from_path
import io
import camelot


def extract_text_from_pdf(pdf):
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_images_from_pdf(pdf):
    images = []
    try:
        pages = convert_from_path(pdf, fmt='png', dpi=200)
        for page in pages:
            image_bytes = io.BytesIO()
            page.save(image_bytes, format='PNG')
            images.append(image_bytes.getvalue())
    except Exception as e:
        st.error(f"Error extracting images: {e}")
    return images

def extract_tables_from_pdf(pdf):
    tables = []
    try:
        camelot_tables = camelot.read_pdf(pdf, pages='all', flavor='stream')
        for table in camelot_tables:
            tables.append(table.df)
    except Exception as e:
        st.error(f"Error extracting tables: {e}")
    return tables

def main():
    st.header("QA Chat Bot with pdf ")

    # Upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type='pdf')

    if pdf is not None:
        text = extract_text_from_pdf(pdf)

        # Extract images and tables
        images = extract_images_from_pdf(pdf)
        tables = extract_tables_from_pdf(pdf)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,  
            chunk_overlap=500,  
            length_function=len
        )
        chunks = text_splitter.split_text(text=text)


if __name__ == '__main__':
    main()
