# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 14:32
# @Author  : 张福隆
# @Email   : 1047366140@qq.com
# @File    : 人人影视.py

import os
import time
import json
import requests
from lxml import etree
from multiprocessing import Pool

#请求部分
def Site(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
    result = requests.get(url,headers=headers)
    result.encoding = "utf-8"
    return result
#解析部分
def Draw(html,xpath):
    html = etree.HTML(html)
    result = html.xpath(xpath)
    return result
#细分部分
def Play(url):
    list = []
    res = Site(url)
    title = Draw(res.text,"//div[@class='page-header']/h4/text()")[0]
    serach = Draw(res.text,"//div[@class='tab_set_info']/p[starts-with(.,'地址列表')]/text()")
    for s in serach:
        value = {}
        link = Draw(res.text, "//div[@class='tab_set_info']/p[starts-with(.,'{}')]/../ul/li/a/@href".format(s))
        for i in range(len(link)):
            value[str(i)] = link[i]
        name = {s:value}
        list.append(name)
    with open("结果/"+title + '.json', 'w', encoding="utf-8") as file:
        file.write(json.dumps(list, indent=2, ensure_ascii=False))
#处理部分
def Central(text):
    title = text
    start = time.time()
    if not os.path.exists("结果"):
        os.mkdir("结果")
    url = "http://yyetss.com/Search/index/?s_keys={}".format(title)
    urls = Draw(Site(url).text,
                "//div[@class='col-xs-3 col-sm-3 col-md-2 min-height-category']/a[@class='imgbox']/@href")
    pool = Pool(processes=8)
    pool.map(Play, urls)
    end = time.time()
    print('进程爬虫耗时:', end - start)
#程序入口
def main():
    Central("美国恐怖故事")

if __name__ == '__main__':
    main()
