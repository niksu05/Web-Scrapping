# Task 3: Fetch Myntra and print the page title

import requests
from bs4 import BeautifulSoup

url = "https://www.myntra.com/"

try:
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=15
    )
    print("Status Code:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    if soup.title:
        print("Page Title:", soup.title.get_text(strip=True))
    else:
        print("Page title was not found in the returned HTML.")
except requests.RequestException as error:
    print("Could not fetch Myntra:", error)
