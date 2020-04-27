# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 14:32
# @Author  : 张福隆
# @Email   : 1047366140@qq.com
# @File    : 签名设计.py
import re
import requests
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

def sign():
    #获取输入姓名
    name = entry.get()
    #优化处理
    name = name.strip()
    if name == "":
        messagebox.showinfo("提示","你没有输入内容")
    else:
        data = {
            'word' :name,
            'sizes': '60',
            'fonts': 'jfcs.ttf',
            'fontcolor': '#000000'
        }
        url = "http://www.uustv.com/"
        result = requests.post(url,data)
        #charset
        result.encoding = "utf-8"
        #正则表达式规则
        reg = r'<div class="tu">﻿<img src="(.*?)"/></div>'
        img_path = re.findall(reg,result.text)
        img_url = url + img_path[0]
        response = requests.get(img_url).content
        with open('{}.gif'.format(name),"wb") as f:
            f.write(response)
        bm = ImageTk.PhotoImage(file='{}.gif'.format(name))
        lable2 = Label(root,image=bm)
        lable2.bm = bm
        lable2.grid(row=2,columnspan=2)

#创建窗口
root = Tk()
#窗口大小，位置
root.geometry("300x300+500+100")
#窗口标题
root.title("设计签名")
#标签控件
lable = Label(root,text="签名",font=('华文行楷',14))
#输入框
entry = Entry(root,font=('华文行楷',14))
#摁钮
button = Button(root,text="设计签名",font=('华文行楷',14),command=sign)
#定位
lable.grid()
entry.grid(row=0,column=1)
button.grid(row=1,column=1)

#显示窗口
root.mainloop()

