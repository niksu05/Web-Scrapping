# Web Scraping — Session 2

## Overview
This session introduces Python libraries used for basic web scraping: `requests` and `BeautifulSoup`.

## Tasks
1. **Setup:** Import `requests` and `BeautifulSoup` to verify that both libraries work.
2. **Flipkart:** Request the homepage and print the first 500 characters of the response.
3. **Myntra:** Parse the returned HTML and print the page title.
4. **Zomato:** Find `<div>` elements and display their unique class names.
5. **BookMyShow:** Find HTML elements that have an `id` attribute and print their tag names and IDs.

## Requirements
- Python 3
- Internet connection
- `requests`
- `beautifulsoup4`

Install the libraries:

```bash
python -m pip install -r requirements.txt
```

## Run the tasks
Run these commands from the `Session-2` folder:

```bash
python task1_setup.py
python task2_flipkart.py
python task3_myntra.py
python task4_zomato.py
python task5_bookmyshow.py
```

## Notes
- Website HTML and output can change over time.
- Some websites may block automated requests or return limited HTML. A `403` status or incomplete result does not always mean the Python code is incorrect.
- This project is for learning. Check each website's terms and `robots.txt`, and only collect public data responsibly. Do not bypass access controls or scrape personal information.

## What I learned
- Installing and importing Python packages
- Sending HTTP GET requests
- Understanding HTML responses
- Parsing HTML with BeautifulSoup
- Finding page titles, `<div>` elements, class names, and `id` attributes
