from BookCatcher_refined1 import Login_Scribd
from time import sleep

#Variaveis
email = ''
password = ''
link = 0
nop = { }
book_urls = [
    
]

scribd = Login_Scribd()

scribd.login(email,password)
#Adição do diretorio nop
for url in book_urls:
    title_and_pages = scribd.get_number_of_pages(url)
    nop.update(title_and_pages)
for book,paginas in nop.items():
    url_in_list = book_urls[link]
    book_for_path = book.replace(' ', '_')
    scribd.take_print(url_in_list, book_for_path, paginas)#Entra no loop de ScreenShots
    link += 1 #Sai do loop e parte pro proximo link adicionando um ao book_url
    