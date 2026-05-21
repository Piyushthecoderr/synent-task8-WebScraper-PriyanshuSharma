import requests
from bs4 import BeautifulSoup

web_Url = "https://books.toscrape.com/"
try:

# response contains response object.It has:
#  Attribute            --> Meaning                           
# response.text        --> extract webpage HTML as plain text
# response.status_code --> success/error code 
# response.headers     --> metadata           
# response.cookies     --> cookies            
    response=requests.get(web_Url)
    if response.status_code==200:

# It will convert messy HTML into searchable structure.html.parser --> uses Python HTML parser to tree.
        soup=BeautifulSoup(response.text,"html.parser") 

# Returns a list like collection of BeautifulSoup Tag objects.
        books=soup.find_all("article",class_="product_pod")
        books_List=[]

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
                "Price":book_Price,
                "Rating":book_Rating,
                "Availability":book_Availability }
            books_List.append(book_Info)

        for item in books_List:
            print(item)
        
    else:
        print("Failed to fetch webpage")
        print("Status code:",response.status_code)
except requests.exceptions.RequestException as e:
    print("Error occured:",e)