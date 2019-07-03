from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import time

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
def search():
    browser.get("http://www.baidu.com")

def next_page(page_number):

    input = wait.until(
        Ec.presence_of_element_located((By.CSS_SELECTOR, '#currentPage')))

    submit = wait.until(Ec.element_to_be_clickable((By.CSS_SELECTOR,'body > form > table > tbody > tr:nth-child(7) > td > input[type="submit"]:nth-child(6)')))

    input.clear()
    input.send_keys(page_number)
    submit.click();
def main():
    search()
    for i in range(2,5):
        next_page(i)
        time.sleep(1.5)
if __name__ == '__main__':
    main()


