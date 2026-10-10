# Task 2: Fetch the first 500 characters of Flipkart HTML

import requests

url = "https://www.flipkart.com/"

try:
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=15
    )
    print("Status Code:", response.status_code)
    print("\nFirst 500 characters of the response:")
    print(response.text[:500])
except requests.RequestException as error:
    print("Could not fetch Flipkart:", error)
