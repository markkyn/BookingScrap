# BookScraping
This python script has as main purpose browserscraping the scribd, an online libary, this way the consumer will be able to "Download" books from PC.

# Requirements:
- Python
- Selenium (Pyhton Lib)
- Scribd Account

# How does this work?
- On "scribd_scraping" there is Classes and Functions which will get the link to login the page, write the email and parameter, and finally get you on consumer page. After that there is a loop that will get each book in the list(main/book_url = []) and take printscreens of each page of the book.

# Funtion's Explanation:
    def login( email, password ):
      - go to the login url('https://pt.scribd.com/login') set on __init__;
      - get 2 inputs(email and password) and 1 button (Login) then send the parameters on "def login" and click the button.
    
    def getnumber_of_pages(book_url):
      - there is 2 url's (on my know) for each book in Scribd, one with "/book/" on its URL and other with "/read/" on its URL;
      - this way, the class getnumber_of_pages go to the "/book/" url and there is a element with the number of the pages of that book
      - with this information in hands another function will use the int number to know how many pages it will have to screenshot before go to the next book.
      -return the variables number of pages and title of the book
      
    def take_print(book_url,books_name, pages):
      -get the list of url's and replace "/book/" for "/read/" as mention on "getnumber_of... / 1"
      -get pages that was retuned by "getnumber_of_pages"
      - this function will take print of each pages ( (pages/2 times ) and click the button that is used to go to the next page( (pages/2) times)
