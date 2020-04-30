# -*- encoding:utf-8 -*-
"""
@作者：张福隆
@时间：2020/03/29
"""
import time
import requests
from selenium import webdriver
from urllib.parse import urlencode
from selenium.webdriver.chrome.options import Options

date = time.strftime("%Y-%m-%d")
# 上报参数
parmers = {
    'id': '',
    'fillDate': date,
    'mqjk': '健康',
    'jrjk': '健康',
    'city1': '黑龙江省',
    'city2': '哈尔滨市',
    'city3': '尚志市',
    'sfwc': '0',
    'sfjc': '0',
    'sfhb': '否',
    'zb': '无',
    'jchz': '否',
    'other': '',
    'other1': '苇河林业局迎宾路',
    'other2': '否',
    'other3': '37.2度及以下 ',
    'other4': '37.2度及以下',
    'other5': '',
    'other6': '否 ',
    'other7': '128.044766,44.735291',
}


def Browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.binary_location = r'C:\Users\linux\AppData\Local\CentBrowser\Application\chrome.exe'
    chrome_path = r'C:\Users\linux\AppData\Local\CentBrowser\Application\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrome_options)
    return driver


def Signin():
    driver = Browser()
    driver.get("http://sso.sdwcvc.cn/")
    driver.find_element_by_id("username").send_keys('2018145051')
    driver.find_element_by_id("password").send_keys('Zfl53497430')
    button = driver.find_element_by_css_selector(".input-group .btn")
    driver.execute_script("arguments[0].click();", button)
    return driver


def Report():
    driver = Signin()
    driver.get("http://pubinfo.sdwcvc.cn/xxtb2/saveRecord?" + urlencode(parmers))
    res = driver.find_element_by_tag_name("PRE")
    return res.text


def Message(mobile, content):
    parmers = {
        'key': 'c448b6079e3042509bf2886581e760a2',
        'mobile': mobile,
        'content': '【智慧山水】' + content + ',您今天的健康信息已上报',
        'tpl_id': 1274
    }
    url = "http://apis.haoservice.com/sms/sendv2?"
    requests.get(url + urlencode(parmers))


def Mistakes(mobile):
    parmers = {
        'key': 'c448b6079e3042509bf2886581e760a2',
        'mobile': mobile,
        'content': '【智慧山水】软件异常，请排查错误',
        'tpl_id': 1350
    }
    url = "http://apis.haoservice.com/sms/sendv2?"
    requests.get(url + urlencode(parmers))


def main():
    try:
        result = eval(Report())
        if (result['status'] == "OK"):
            print("成功")
            Message(15304619319, "张福隆")
    except:
        print("软件异常")
        Mistakes(15304619319)
if __name__ == "__main__":
    main()
