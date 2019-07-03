import json
import re
import requests
from requests.exceptions import RequestException


def get_one_page(url):
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
               "Accept-Encoding": "gzip",
               "Accept-Language": "zh-CN,zh;q=0.8",
               "Referer": "http://www.example.com/",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"}
    response = requests.get(url,headers=headers)
    #print(response.status_code)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
def parse_on_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
    +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
    +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            "index":item[0],
            "image":item[1],
            "title":item[2],
            "actor":item[3].strip()[3:],
            "time":item[4].strip()[5:],
            "score":item[5]+item[6]
        }
def write_to_file(content):
    with open("result.txt","a") as f:
        f.write(json.dumps(content)+"\n")
        f.close()


def main(offset):
    url = "http://maoyan.com/board/4?offset="+str(offset)
    html = get_one_page(url)
    for item in parse_on_page(html):
        print(item)
        write_to_file(item)
    # print(html)
if __name__ =='__main__':
    for i in range(10):
        main(i*10)

