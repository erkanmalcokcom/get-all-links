import argparse
import os
import sys
import fitz  # PyMuPDF
import openai
from prettytable import PrettyTable

# Fetch the OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    print("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    sys.exit(1)
openai.api_key = api_key

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    try:
        with fitz.open(pdf_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        raise RuntimeError(f"Could not read PDF file: {pdf_path}. Error: {str(e)}")

def summarize_document_content(content):
    """Summarize the content of a document."""
    try:
        # Simulating a conversational approach for summarization
        summary_response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Summarize this document content: {content[:4000]}"}
            ]
        )
        summary_text = summary_response.choices[0].message.content.strip()
        return summary_text
    except Exception as e:
        raise RuntimeError(f"Error summarizing document content: {str(e)}")

def categorize_and_summarize_files(download_dir):
    """Categorize and summarize PDF files in a directory."""
    if not os.path.exists(download_dir):
        print(f"Directory {download_dir} does not exist.")
        return

    abs_download_dir = os.path.abspath(download_dir)
    print(f"Scanning directory: {abs_download_dir}")

    # Create a table with headers
    summary_table = PrettyTable()
    summary_table.field_names = ["File Name", "Summary"]

    for filename in os.listdir(abs_download_dir):
        filepath = os.path.join(abs_download_dir, filename)
        if filepath.endswith('.pdf'):
            try:
                # print(f"Processing file: {filepath}")
                pdf_text = extract_text_from_pdf(filepath)
                summary_text = summarize_document_content(pdf_text)
                summary_table.add_row([filename, summary_text])

            except Exception as e:
                print(f"Error processing file {filename}: {str(e)}")

    # Print the table after processing all files
    print(summary_table)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='PDF Categorizer and Summarizer')
    parser.add_argument('-d', '--directory', required=True, help='Directory containing downloaded PDF files')
    args = parser.parse_args()

    categorize_and_summarize_files(args.directory)
