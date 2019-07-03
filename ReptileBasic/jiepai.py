from urllib.parse import urlencode
#https://www.toutiao.com/a6602198402644050436/
import json
import re
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import requests


def get_page_index(offset,keyword):
    data= {
        "offset": offset,
        "format": "json",
        "keyword": keyword,
        "autoload": "true",
        "count": "20",
        "cur_tab": 1

    }
    url = "https://www.toutiao.com/search_content/?"+urlencode(data)

  #  print(response.status_code)
    try:
        response = requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        print("请求失败")
        return None
def parse_page_loads(html):
    data = json.loads(html)
    if data and "data" in data.keys():
        for item in data.get("data"):
            yield  item.get("article_url")
def get_page_detail(url):
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
               "Accept-Encoding": "gzip",
               "Accept-Language": "zh-CN,zh;q=0.8",
               "Referer": "http://www.example.com/",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"}
    try:
        response = requests.get(url,headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求失败啊",url)
        return None
def parse_page_detail(html):
    soup = BeautifulSoup(html,"lxml")
    title = soup.select("title")[0].get_text()
    images_pattern = re.compile()

def main():
    html = get_page_index(0,"街拍")
    for url in parse_page_loads(html):
        html = get_page_detail(url)

if __name__ == '__main__':
    main()
