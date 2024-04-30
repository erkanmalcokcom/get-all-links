# Web Content Downloader

The Web Content Downloader is a Python application that allows you to download files linked on a webpage. It utilizes the BeautifulSoup library for parsing HTML and the requests library for making HTTP requests.

- Download files linked on a webpage by providing a URL.
- Option to use local HTML files found in the root directory.

### Installation
1. Clone this repository to your local machine.
2. Ensure you have Python installed on your system.
3. Install the required dependencies by running:
    ```
    pip install beautifulsoup4 requests
    ```
4. Run the `web_content_downloader.py` script to start the application.

### Usage

1. **If you have a URL:**

    - Run the script and provide the URL when prompted.
    
    ```
    $ python web_content_downloader.py
    ```

2. **If you have local HTML files:**

    - Place the HTML file(s) in the root directory of the application.
    
    - Run the script and select the option to use the local HTML file(s) when prompted.
    
    ```
    $ python web_content_downloader.py
    ```
