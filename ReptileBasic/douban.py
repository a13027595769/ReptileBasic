import requests
from bs4 import BeautifulSoup
import re

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
           "Accept-Encoding": "gzip",
           "Accept-Language": "zh-CN,zh;q=0.8",
           "Referer": "http://www.example.com/",
           "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"}
content = requests.get("https://book.douban.com/",headers=headers).text
soup = BeautifulSoup(content,"lxml")
# print(soup.title)
# print(soup.head)
# print(soup.p.string)#
# print(soup.p.children)
# for i,child in enumerate(soup.p.children):
#     print(i,child)
# print(soup.parent)
pattern = re.compile('<li.*?cover">.*?href="(.*?)".*?title="(.*?)".*?more-meta">.*?title>".*?(.*?)</h4>.*?</li>',re.S)

results = re.findall(pattern,content)
for result in results:
    url,name,author,date = result
    print(url,name,author,date)
