# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 19:44
# @Author  : 张福隆
# @Email   : 1047366140@qq.com
# @File    : 百度图片.py
import re
import json
import time
import requests
from lxml import etree
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
'''
爬取百度图片，页面向下拉到底，会加载新的网页数据。
'''
def Driver(word,min):
    # 创建浏览器对象
    browser = webdriver.Chrome(executable_path=r'C:\Users\linux\AppData\Local\CentBrowser\Application\chromedriver.exe')
    # 设置加载超时时间
    wait = WebDriverWait(browser,20)
    browser.get("https://image.baidu.com/")
    browser.find_element_by_id('kw').send_keys(word)
    browser.find_element_by_xpath("//span[@class='s_search']").click()
    browser.implicitly_wait(30)
    thred = 0
    while thred<=min:
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        thred = thred + 1
        time.sleep(1) #休眠一秒
    html = etree.HTML(browser.page_source)
    result = str(html.xpath("//div[@id='resultInfo']/text()")[0])
    result = re.sub("\D", "", result)
    print(result)
    return result

def Site(word,min):
    page = int(Driver(word,min))
    for pn in range(0,page,30):
        res = requests.get("https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&word={}&pn={}&rn=30".format(word,pn))
        res = re.findall(r'"thumbURL":".*?.jpg"', res.text)
        with open(word+".txt", "a") as f:
            for i in res:
                res = re.findall(r'http[s]?://.*?.jpg', i)
                f.write(res[0])
                f.write("\n")
def main():
    Site("杨幂",120)
if __name__ == '__main__':
    main()






