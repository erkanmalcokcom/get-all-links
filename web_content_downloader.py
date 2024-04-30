import argparse
from bs4 import BeautifulSoup
import requests
import os
from urllib.parse import urlparse, urljoin

def ensure_download_directory(directory='downloads'):
    """Ensure the download directory exists, create if it does not."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")
    return directory

def find_html_files(directory):
    """Scan a directory and return a list of HTML file paths."""
    if os.path.isdir(directory):
        html_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.html')]
        return html_files
    elif os.path.isfile(directory) and directory.endswith('.html'):
        return [directory]  # Treat the directory argument as a single HTML file path
    else:
        return []

def download_links_from_html(source, download_dir='downloads'):
    download_dir = ensure_download_directory(download_dir)
    log_file_path = os.path.join(download_dir, 'downloaded_files.log')

    # Load the HTML content
    with open(source, 'r') as file:
        html_content = file.read()
    base_url = None

    # Track downloaded files
    downloaded_files = set()
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as f:
            downloaded_files.update(f.read().splitlines())

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    # links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith(tuple(['.pdf', '.doc', '.xls']))]
    links = list(set(a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith(tuple(['.pdf', '.doc', '.xls']))))

    # Download the linked files
    for link in links:
        absolute_link = urljoin(base_url, link) if base_url else link
        filename = os.path.basename(urlparse(link).path)
        filepath = os.path.join(download_dir, filename)

        if filename not in downloaded_files:
            try:
                response = requests.get(absolute_link)
                if response.status_code == 200:
                    with open(filepath, 'wb') as file:
                        file.write(response.content)
                    print(f"Downloaded {filename} to {filepath}")
                    with open(log_file_path, 'a') as f:
                        f.write(filename + '\n')
                else:
                    print(f"Failed to download {filename}. HTTP Status Code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to download {filename}. Error: {e}")
        else:
            print(f"Skipped {filename}, already downloaded.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Web Content Downloader')
    parser.add_argument('source', nargs='?', default='index.html', help='Path to the HTML file or directory to download content from')
    args = parser.parse_args()

    download_dir = ensure_download_directory()
    if os.path.exists(args.source):
        html_files = find_html_files(args.source)
        for html_file in html_files:
            print(f"Processing {html_file}")
            download_links_from_html(html_file, download_dir)
    else:
        print(f"No valid HTML file or directory found at {args.source}. Using default 'index.html'.")
        if os.path.exists('index.html'):
            download_links_from_html('index.html', download_dir)
        else:
            print("Default file 'index.html' not found.")
