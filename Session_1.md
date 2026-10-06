# Web-Scrapping
Web Scrapping Assignment
# Session 1 - Introduction to Web Scraping

## Introduction

Web scraping is the process of automatically collecting data from websites using software or Python programs.

Python provides libraries such as `requests` and `BeautifulSoup` that make it easier to download and extract information from web pages.

## Task 1 - Flipkart

**Website:** Flipkart

**HTML Tag:** `<div>`

**Class Name:** `RG5Slk`

**Product Title:** HP 15 Intel Core 5 120U - (16 GB/512 GB SSD/Windows 11 Home)

The `<div>` element with the class `RG5Slk` contains the product title.



## Task 2 - Zomato robots.txt

### Rule 1

User-agent: *
Disallow: /

**Explanation:**  
This rule applies to all bots/crawlers that do not have a more specific rule. 
`Disallow: /` tells these bots not to crawl any part of the Zomato website.

### Rule 2

User-agent: Googlebot
Disallow: /admin/
Disallow: /users/
Disallow: /downloads/
Allow: /

**Explanation:**  
For Googlebot, Zomato allows crawling of the website generally using 
`Allow: /`, but specifically disallows sensitive or restricted paths such 
as `/admin/`, `/users/`, and `/downloads/`.



## Task 3 - Myntra vs Instagram

### Myntra:
When we open Myntra, we can see most of the main content on the page. Some extra data is loaded through additional requests.

### Instagram:
Instagram loads its content differently. Many posts and other details are loaded after the page opens using JavaScript and API requests. So, if we only get the initial HTML, we may not see all the content shown on Instagram.



## Task 4 - Inspect HTTP Request Headers on BookMyShow

## Steps I Followed

1. Opened BookMyShow in Google Chrome.
2. Opened Chrome Developer Tools.
3. Selected the **Network** tab.
4. Refreshed the BookMyShow webpage.
5. Selected the main page request.
6. Opened the **Headers** section.
7. Found the `User-Agent` under Request Headers.

## User-Agent

The User-Agent shown in my browser was:
    user-agent
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36


