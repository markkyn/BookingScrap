from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from time import sleep

class Login_Scribd:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,100)
        self.login_URL = 'https://pt.scribd.com/login'  
        

    def login(self,email, password):
        self.driver.get(self.login_URL)

        try:
            self.driver.find_element_by_id('login_or_email').send_keys(email)
            self.driver.find_element_by_id('login_password').send_keys(password)
            self.driver.find_element_by_class_name('button_container').click()
            self.wait.until(EC.url_changes(self.login_URL))
            

        except NoSuchElementException:
            self.driver.quit()
            print('NoSuchElementException')
    

    def get_number_of_pages(self, book_url):
        self.book_url = book_url

        self.driver.get(book_url)

        pages_element = self.driver.find_element_by_css_selector('span[class="info_span"]')
        title_element = self.driver.find_element_by_css_selector('h1[class="document_title"')

        text_of_pages = pages_element.text
        title = title_element.text

        number_of_pages = int(text_of_pages.replace('páginas',''))
        return { title : number_of_pages }
        
    def take_print(self,book_url,books_name, pages):
        read_url = book_url.replace('/book/','/read/')
        self.driver.get(read_url)
        sleep(10)

        next_page = self.driver.find_element_by_css_selector('button[class="page_right next_btn"]')
        percentage_read = int(self.driver.find_element_by_css_selector('div[class="percentage_read"').text.replace('% lido',''))
        like_the_book = self.driver.find_element_by_css_selector('span[class="icon icon-ic_close"')
        try:
         self.driver.find_element_by_css_selector('a[class="icon icon-ic_close"]').click() #popup
        except NoSuchElementException:
            pass
        except ElementNotInteractableException:
            pass

        for i in range(pages):
            try:
                like_the_book.click()
            except NoSuchElementException:
                pass
            except ElementNotInteractableException:
                pass
            sleep(2)
            self.driver.save_screenshot('%s_%i' % (books_name,i)+'.png')
            if percentage_read < 100:
                next_page.click()
            elif percentage_read == 100:
                break
            


