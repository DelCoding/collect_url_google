# coding: UTF-8
import re

content = open('html.txt','rb')
tt = content.read().decode('utf-8')

def getList(regex,text):
    arr = []
    text = re.sub("div","\n",text)
    res = re.findall(regex, text)
    if res:
        for r in res:
            arr.append(r)
    return arr

arrList = getList(r'event\)\">(.*)</a><img', tt)
arrList2 = getList(r'\"_Rm\">(.*)/.*</cite><', tt)

print (len(arrList))
print (len(arrList2))
print(arrList)
print(arrList2)
save = open('result.txt','a+')
for url, name in zip(arrList2,arrList):
    strs = url + " " + name + "\n"
    print (strs)
    save.write(strs)

save.close()
