import requests
from bs4 import BeautifulSoup

def fetch_Page(url):
    response=requests.get(url,timeout=10)
    if response.status_code != 200:
        print("Failed to fetch webpage")
        print("Status code:",response.status_code)
        return None
    return response

def extract_Books(html_Content):

    # It will convert messy HTML into searchable structure. html.parser --> uses Python HTML parser to tree.
    soup=BeautifulSoup(html_Content,"html.parser")

    # Returns a list like collection of BeautifulSoup Tag objects.
    books=soup.find_all("article",class_="product_pod")

    books_List=[]
    # each item in books points to one BeautifulSoup Tag object,representing one complete <article> HTML section.
    for item_book in books:
        book_Title=item_book.h3.a["title"]
        book_Price=item_book.find("p",class_="price_color").text

        # book.find("p",class_="star-rating")["class"] returns something like:['star-rating','Three']
        # [1] ensures to return second class name,which represents actual rating.
        book_Rating=item_book.find("p",class_="star-rating")["class"][1]
        book_Availability=item_book.find("p",class_="instock availability").text.strip()
        book_Info={
            "Title":book_Title,
            "Cost":book_Price,
            "Rating":book_Rating,
            "Availability":book_Availability
                }
        books_List.append(book_Info)
    return books_List