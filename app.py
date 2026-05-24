import requests
from scraping import fetch_Page
from scraping import extract_Books
from exports import save_CSV
from exports import save_JSON

base_Url="https://books.toscrape.com/catalogue/page-{}.html"
all_Books=[]
try:

    # response contains response object.
    # It has:
    # response.text
    # response.status_code
    # response.headers
    # response.cookies

    for page_Number in range(1, 51):
        if page_Number == 1:
            current_Url = "https://books.toscrape.com/"
        else:
            current_Url = base_Url.format(page_Number)

        print(f"Scraping page {page_Number}...")
        response=fetch_Page(current_Url)

        if response is None:
            break

        page_Books = extract_Books(response.text)
        all_Books.extend(page_Books)
    save_CSV(all_Books)
    save_JSON(all_Books)

except requests.exceptions.RequestException as e:
    print("Error occurred:", e)