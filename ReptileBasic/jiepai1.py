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

def main():
    html = get_page_index(0,"街拍")
    print(html)

if __name__ == '__main__':
    main()
