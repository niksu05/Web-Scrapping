# Task 4: Find unique class names used in Zomato <div> elements

import requests
from bs4 import BeautifulSoup

url = "https://www.zomato.com/"

try:
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=15
    )
    print("Status Code:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    divs = soup.find_all("div")

    unique_classes = set()

    for div in divs:
        classes = div.get("class")
        if classes:
            for class_name in classes:
                unique_classes.add(class_name)

    print("Total unique class names:", len(unique_classes))
    print("\nUnique class names:")
    for class_name in sorted(unique_classes):
        print(class_name)

except requests.RequestException as error:
    print("Could not fetch Zomato:", error)
