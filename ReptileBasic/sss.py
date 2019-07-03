# import urllib.request
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))
import requests                       #用来请求网页
from bs4 import BeautifulSoup         #解析网页
import time          #设置延时时间，防止爬取过于频繁被封IP号
import re            #正则表达式库
import pymysql       #由于爬取的数据太多，我们要把他存入MySQL数据库中，这个库用于连接数据库
import random
url="https://book.douban.com/tag/?icn=index-nav"
wb_data=requests.get(url)                #请求网址
soup=BeautifulSoup(wb_data.text,"lxml")  #解析网页信息
tags=soup.select("#content > div > div.article > div > div > table > tbody > tr > td > a")
     #根据CSS路径查找标签信息，CSS路径获取方法，右键-检查-copy selector，tags返回的是一个列表
for tag in tags:
       tag=tag.get_text()    #将列表中的每一个标签信息提取出来
       helf="https://book.douban.com/tag/"
          #观察一下豆瓣的网址，基本都是这部分加上标签信息，所以我们要组装网址，用于爬取标签详情页
       url=helf+str(tag)
       print(url)    #网址组装完毕，输出
