#coding: UTF-8

from selenium import webdriver
import re
import time

browser = webdriver.Chrome()

def getList(regex,text):
    arr = []
    text = re.sub("div","\n",text)
    res = re.findall(regex, text)
    if res:
        for r in res:
            arr.append(r)
    return arr

def core(html):
    title_arr = getList(r'event\)\">(.*)</a><img', html)
    url_arr = getList(r'\"_Rm\">(.*)/.*</cite><', html)
    sums = 0
    file = open('result.txt', 'a+')
    for url,title in zip(url_arr,title_arr):
        strs = url + " " + title + "\n"
        file.write(strs)
        #print(strs)
        sums += 1

    print('写入：' + str(sums) + '个记录')

def search(keyword,pages):
    url = "https://www.google.com"
    browser.get(url)
    inputs = browser.find_element_by_name('q')
    inputs.send_keys(keyword)
    button = browser.find_element_by_name('btnK')

    for n in range(pages):
        button.click()
        page = n + 1
        print('正在搜索第 ' + str(page) + ' 页')
        time.sleep(4)
        html = browser.page_source
        core(html)
        button = browser.find_element_by_id('pnnext')
    browser.close()


if __name__ == '__main__':
    keyword = input('请输入搜索关键字：')
    pages = input('请输入页数：')
    pages = int(pages)
    search(keyword, pages)