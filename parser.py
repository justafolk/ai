import requests
from bs4 import BeautifulSoup

# URL to fetch content from
url = "https://gilberttanner.com/blog/introduction-to-data-visualization-inpython/"  # Replace with the URL you want to scrape

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <pre> tags with class="language-python"
        python_code_blocks = soup.find_all('code', class_='language-python')

        # Print the content of each <pre> tag
        for code_block in python_code_blocks:

            print("#-------------------------------")
            print(code_block.get_text())
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {str(e)}")

