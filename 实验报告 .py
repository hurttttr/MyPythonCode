import os
import re
import sys
import io
from urllib import request
import pdfkit
import requests

sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码


def getCookie():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    first_url = 'http://10.132.246.246'  # 网站的首页
    session = requests.session()
    response = session.get(first_url, headers=headers)

    print(response.cookies)
    token = response.cookies.items()[0][1]  # 获得token
    print(token)
    username = '19211860109'
    password = "123456qwer"

    data = {  # 登录所需的账号、密码、token
        'username': username,
        'password': password,
        'csrfmiddlewaretoken': token
    }
    # 登录url
    login_url = 'http://10.132.246.246/user/logincheck/'  # 登录接口

    response = session.post(login_url, data=data, headers=headers)
    cookie_str = response.request.headers['Cookie']
    print(response.request.headers['Cookie'])
    print(response.status_code)  # 打印状态码，看是否请求成功
    return cookie_str


# 登录后才能访问的网站
url = 'http://10.132.246.246/course/100/detail/'

# 浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = getCookie()

str1 = cookie_str.split(';')
token = str1[0].split('=')[1]
session = str1[1].split('=')[1]
cookie_options = {

    'cookie': [('csrftoken', token), ('sessionid', session), ],
}


req = request.Request(url)
# 设置cookie
req.add_header('cookie', cookie_str)
# 设置请求头
req.add_header(
    'User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

resp = request.urlopen(req)

html = resp.read().decode('utf-8')

print(html)


def save_to_pdf(url, filename):
    # 本来直接调用pdfkid的from方法就可以了，但是由于我们的wkhtmltopdf安装包有点问题，一直没法搜到，所以只能用本办法，直接配置了wk的地址
    # wkhtmltopdf下载链接： https://wkhtmltopdf.org/downloads.html
    config = pdfkit.configuration(
        wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdfkit.from_url(url, filename, configuration=config,
                    options=cookie_options)


if not os.path.exists("D:\\ftp1"):
    os.mkdir("D:\\ftp1")

list1 = []  # 存链接
list2 = []  # 废弃
list3 = []
name = []  # 存标题

# print(data)
a = html.find('<td ><a href="')
while a != -1:
    b = html.find('">', a, a+50)
    if b != -1:
        # print(html[a+14:b-1])
        list1.append(html[a+14:b-1])
    else:
        b = a+5
    a = html.find('<td ><a href="', b)

name = re.findall('<td ><a href=".*?"> (.*?) </a> </td>', html)
for each in name:
    if not os.path.exists("D:\\ftp1\\" + each):
        os.mkdir("D:\\ftp1\\" + each)

# print(list2)
# 各个章节处理完毕

for url_index in range(len(list1)):
    # release()
    purl = list1[url_index]
    # pyautogui.sleep(2)#防止被拦截
    urls = 'http://10.132.246.246'  # 前缀，可根据是否使用webvpn修改
    # webbrowser.open(urls+purl)
    print(urls+purl)

    # 登录后才能访问的网站
    url = urls+purl

    req = request.Request(url)
    # 设置cookie
    req.add_header('cookie', cookie_str)
    # 设置请求头
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

    resp = request.urlopen(req)

    html = resp.read().decode('utf-8')

    # print(html)
    list3.clear()
    list3 = re.findall('<td><a href="(.*?)&result=AC">', html)
    urls1 = '&result=AC'
    print(list3)

    # head="D:\\ftp\\"+list2[url_index]+'\\'
    # print(name[[url_index]])

    for hurl in list3:

        url = urls + hurl + urls1

        req = request.Request(url)
        # 设置cookie
        req.add_header('cookie', cookie_str)
        # 设置请求头
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

        resp = request.urlopen(req)

        html = resp.read().decode('utf-8')

        # addr = re.findall('<a href="/judge/.
        # *?/course/100/"> (.*?)</a> </td>', html)
        a = html.find('<td><a href="/judge/')
        # b=html.find('',a,a+100)
        addr = html[a+20:a+27]
        print(addr)

        if name[url_index].find('实验') != -1:
            raddr = 'http://10.132.246.246/judge/' + addr + '/course/100/print_exp/'
        else:
            raddr = 'http://10.132.246' \
                    '.246/judge/' + addr + '/course/100/print_ass/'

        p = str(name[url_index])
        pp = "D:\\ftp1\\"+p+'\\'

        a = html.find('<td ><a href="/courseproblem/')
        # b=html.find('',a,a+100)
        oo = html[a + 29:a + 33]
        print(oo)

        qq = 'AC-20211860126-杨洋- 题号'+oo+'-判题编号_'+addr+'.pdf'
        save_to_pdf(raddr, pp+qq)
        print(qq+'保存成功！')
