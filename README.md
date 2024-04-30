# Web Content Downloader

The Web Content Downloader is a Python-based utility designed to facilitate the downloading of files linked within a webpage. Utilizing the BeautifulSoup library to parse HTML content and the requests library to handle HTTP requests, this application is perfect for anyone looking to automate the downloading of resources from the web.

## Features

- **Download Links**: Automatically download files linked from a specific webpage.
- **Local HTML Support**: Process local HTML files to extract and download linked files.
- **User-Friendly**: Simple command-line interface for easy operation.
- **PDF Categorization and Summarization**: Analyze PDF documents to classify and summarize their contents, displaying the results in an easy-to-read table format.


## Installation

Follow these steps to set up the Web Content Downloader on your local machine:

1. **Obtain the project files by cloning this repository.**
   ```bash
   git clone https://github.com/erkanmalcokcom/web_content_downloader.git
   ```

2. **Prerequisites**
   - Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. **Navigate to the project directory and install the required Python libraries:**
   ```bash
   cd web_content_downloader
   pip install beautifulsoup4 requests
   ```

## Usage

You can use the Web Content Downloader in two ways depending on the source of the HTML content:

### Using a URL

1. Execute the script from the command line and follow the prompts to input the URL of the webpage:
   ```bash
   python web_content_downloader.py --url https://example.com
   ```

### Using Local HTML Files

1. Place your local HTML file(s) in the project directory.
2. Run the script and it will automatically detect and process files from the directory:
   ```bash
   python web_content_downloader.py --file filename.html
   ```

### Summarizing PDF Documents
To categorize and summarize PDF files, place them in a specified directory and run the summarization script:
bash
Copy code
python summarize_app.py --directory downloads/0001.pdf


## Configuration Options

The script offers several configuration options that you can adjust according to your needs, such as specifying output directories or filtering file types to download.

## Contributions

Contributions to the Web Content Downloader are welcome. Please feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is licensed under the MIT License.
```

### Key Components of the README:

- **Introduction**: A brief introduction about what the tool does and its primary features.
- **Installation**: Step-by-step instructions on how to get the project up and running.
- **Usage**: Details on how to use the application, including both URL and local HTML file processing.
- **Configuration Options**: Mention of configurable aspects of the script to tailor it to specific needs.
- **Contributions**: Encouragement for community involvement in improving the project.
- **License**: Information on the project's license.

This README should provide all necessary information to get started with the Web Content Downloader, from setup to everyday use.