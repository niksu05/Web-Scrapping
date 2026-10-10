# Task 5: Find HTML elements with an id attribute on BookMyShow

import requests
from bs4 import BeautifulSoup

url = "https://in.bookmyshow.com/explore/home/ahmedabad"

try:
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=15
    )
    print("Status Code:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.find_all(id=True)

    print("Total elements with an id attribute:", len(elements))
    print("\nTag names and IDs:")
    for element in elements:
        print(f"Tag: {element.name} | ID: {element.get('id')}")

except requests.RequestException as error:
    print("Could not fetch BookMyShow:", error)
