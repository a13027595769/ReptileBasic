from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import time

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
def search():
    browser.get("http://localhost/product")
    input = wait.until(
        Ec.presence_of_element_located((By.CSS_SELECTOR, '#kw'))
    )
   # input1 = wait.until(
    #    Ec.presence_of_element_located((By.CSS_SELECTOR, 'body > form > input[type="text"]:nth-child(2)'))
    #)
    #input2 = wait.until(
    #    Ec.presence_of_element_located((By.CSS_SELECTOR, 'body > form > input[type="text"]:nth-child(3)'))
    #)


    submit = wait.until(Ec.element_to_be_clickable((By.CSS_SELECTOR,"#su")))



    input.send_keys("美食")
    #input1.send_keys(u"100")
    #input2.send_keys(u'200')
    submit.click()
def main():
    search()
if __name__ == '__main__':
    main()


