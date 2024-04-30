from bs4 import BeautifulSoup
import requests
import os
import glob

download_dir = 'downloads'

if not os.path.exists(download_dir):
    os.makedirs(download_dir)
    print(f"Created {download_dir}")

# Check if there is any HTML file in the root directory
if glob.glob("./*.html"):
    user_input = input("HTML file(s) found in the root directory. What would you like to do? ")
else:
    html_source = input("Enter the URL to download: ")

soup = BeautifulSoup(requests.get(html_source).content, 'html.parser')
links = [a['href'] for a in soup.find_all('a', href=True)]

for link in links:
    filename = link.split('/')[-1]
    filepath = os.path.join(download_dir, filename)
    with open(filepath, 'wb') as file:
        response = requests.get(link)
        file.write(response.content)
    print(f"Downloaded {filename}")