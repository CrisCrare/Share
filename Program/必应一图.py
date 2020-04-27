# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 14:32
# @Author  : 张福隆
# @Email   : 1047366140@qq.com
# @File    : 必应一图.py
import requests
import json
import time
url_head = 'https://www.bing.com/'
url_res = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'

def request(url):#请求网址
    res = requests.get(url)
    return res
def Preser(url):#保存图片
    with open(time.strftime('%Y-%m-%d')+".jpg","wb") as w:
        w.write(request(url).content) 
if __name__ == "__main__":
    url_foot = json.loads(request(url_res).text)#序列化字符串
    url = url_head + url_foot["images"][0]['url'] #拼接网址
    Preser(url)