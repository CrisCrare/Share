# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 14:32
# @Author  : 张福隆
# @Email   : 1047366140@qq.com
# @File    : 中英互译.py

import requests
from tkinter import *
from tkinter import messagebox


def translation():
    text = entry1.get()
    text = text.strip()
    if text == "":
        messagebox.showinfo("提示", "你没有输入内容")
    else:

        data = {
            'i': text,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        result = requests.post(url, data).json() #转换json字节码
        tran = result['translateResult'][0][0]['tgt']
        res.set(tran)
        return tran


window = Tk()
window.geometry('350x100')
window.title("中英互译")
lable1 = Label(window, text="输入要翻译的文字：", font=("微软雅黑", 12))
lable1.grid()
entry1 = Entry(window, font=("微软雅黑", 12))
entry1.grid(row=0, column=1)
lable2 = Label(window, text="翻译之后的结果：", font=("微软雅黑", 12))
lable2.grid(row=1, column=0)
res = StringVar()
entry2 = Entry(window, font=("微软雅黑", 12),textvariable=res)
entry2.grid(row=1, column=1)

button1 = Button(window, text="翻译", width=10, command=translation)
button1.grid(row=2, column=0, sticky=W)
button2 = Button(window, text="退出", width=10, command=window.quit)
button2.grid(row=2, column=1, sticky=E, )

window.mainloop()
