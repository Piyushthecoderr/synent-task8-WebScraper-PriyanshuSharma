import csv
import json
import requests
from bs4 import BeautifulSoup

base_Url = "https://books.toscrape.com/catalogue/page-{}.html"
books_List=[]
try:

# response contains response object.It has:
#  Attribute            --> Meaning                           
# response.text        --> extract webpage HTML as plain text
# response.status_code --> success/error code 
# response.headers     --> metadata           
# response.cookies     --> cookies            
    for page_Number in range(1, 51):
        if page_Number == 1:
            current_Url="https://books.toscrape.com/"
        else:
            current_Url=base_Url.format(page_Number)

        print(f"Wait! Scraping page {page_Number}...")
        response=requests.get(current_Url,timeout=10)

        if response.status_code != 200:
            print("Failed to fetch webpage")
            print("Status code:",response.status_code)
            break

# It will convert messy HTML into searchable structure.html.parser --> uses Python HTML parser to tree.
        soup=BeautifulSoup(response.text,"html.parser") 

# Returns a list like collection of BeautifulSoup Tag objects.
        books=soup.find_all("article",class_="product_pod")

# each item in books point to one BeautifulSoup Tag object repersenting one complete <article> HTML section with class="prouct_pod".
        for item_book in books:
            book_Title=item_book.h3.a["title"]
            book_Price=item_book.find("p",class_="price_color").text

    # book.find("p",class_="star-rating")["class"] will return sth. like ['star-rating','Three'] i.e multiple class for same tag.
    # [1] ensures to return second class name which repersents actual rating.
            book_Rating=item_book.find("p",class_="star-rating")["class"][1]
            book_Availability=item_book.find("p",class_="instock availability").text.strip()
            book_Info={
                "Title":book_Title,
                "Cost":book_Price,
                "Rating":book_Rating,
                "Availability":book_Availability }
            books_List.append(book_Info)
        
            
    with open("data/books.csv","w",newline="",encoding="utf-8") as csvFile:
        fieldnames=["Title","Cost","Rating","Availability"]
        writer=csv.DictWriter(csvFile,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books_List)
    print("Successful creation of CSV File")

    with open("data/books.json","w",encoding="utf-8") as jsonFile:
        json.dump(books_List,jsonFile, indent=4)
    print("Successful creation of JSON File") 
        
except requests.exceptions.RequestException as e:
    print("Error occurred:",e)