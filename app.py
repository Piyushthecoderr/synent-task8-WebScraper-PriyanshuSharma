import requests
from scraping import fetch_Page
from scraping import extract_Books
from exports import save_CSV
from exports import save_JSON
import time
from datetime import datetime

# headers dictionary stores HTTP request headers.
# Headers provide extra metadata/information to website servers about the client making the request.

# "User-Agent" is a standard HTTP header used to identify browser/client information.

# "Mozilla/5.0" -->h istorical browser compatibility string.
# Modern browsers include it in User-Agent to follow compatibility conventions expected by websites.

# "Windows NT 10.0" --> Windows 10 operating system.

# "Win64" --> 64-bit Windows operating system.

# "x64" --> x86-64 CPU architecture.

# "AppleWebKit/537.36" represents browser rendering engine,compatibility information and WebKit engine version details.

# "(KHTML, like Gecko)" means browser behaves similarly to modern Gecko-compatible browsers for website compatibility.

# "Chrome/125.0" represents Google Chrome browser version 125.

# "Safari/537.36" is additional browser compatibility information.

# All these values are used to make request appear more like a normal real browser request instead of just anonymous bot request.
# These values are public browser identification strings.

request_Headers={
    "User-Agent":(
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/125.0 Safari/537.36"
                )
               }
base_Url="https://books.toscrape.com/catalogue/page-{}.html"
all_Books=[]
try:

    # response contains response object.
    # It has:
    # response.text
    # response.status_code
    # response.headers
    # response.cookies

    for page_Number in range(1,51):
        if page_Number == 1:
            current_Url = "https://books.toscrape.com/"
        else:
            current_Url = base_Url.format(page_Number)

        current_Time=datetime.now().strftime("%A %Y-%m-%d %H:%M:%S")
        print(f"[{current_Time}] " f"Scraping page {page_Number}...")
        response=fetch_Page(current_Url,request_Headers)
        if response is None:
            break

        page_Books=extract_Books(response.text)
        all_Books.extend(page_Books)
        print(f"Books scraped from page {page_Number}:{len(page_Books)}")
        time.sleep(1)
    save_CSV(all_Books)
    save_JSON(all_Books)
    print("\nTotal Pages Scraped:50")
    print(f"Total books scraped:{len(all_Books)}")
    print("Scraping completed successfully")

except requests.exceptions.RequestException as e:
    print("Error occurred:", e)