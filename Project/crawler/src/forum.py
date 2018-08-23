#coding=utf-8
import urllib
import re
import os
import urllib.request
import requests

def getHtml(url):
    #input：网址
    #output：html文本
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getItems(html):
    #input： 列表页
    #output 该列表页的子链接
    reg = r'thread[0-9\-]*\.html'
    urlre = re.compile(reg)
    items = re.findall(urlre,html)
    return items

def getImg(insideUrl):
    #input: 子链接
    #output: 图片链接
    reg = r'src="http(.*)jpg'
    #reg2 = r'img src="http(.*)png'
    urlre = re.compile(reg)
    html = getHtml(insideUrl)
    html = html.decode('utf-8','ignore')#python3
    #print(html)
    imgUrl = re.findall(urlre,html)
    last = r'jpg'
    if len(imgUrl) < 1:
        reg = r'img src="http(.*)png'
        urlre = re.compile(reg)
        imgUrl = re.findall(urlre,html)
        last = r'png'
    #print('img:   ',imgUrl)
    imgPoster = imgUrl[0]
    return 'http'+imgPoster+last


#part 1  获取每个列表页的内页链接 
for i in range(7,10):
    raw_url = "xxxxx%s.html" % i
    html = getHtml(raw_url)
    html = html.decode('utf-8','ignore')#python3

    items = getItems(html)
    items = list(set(items))
    #print('items:   ',items)
    savePath = '/Users/fire/A/workshop/pachong/sis/result/%s/' % i
    isExists=os.path.exists(savePath)
    if not isExists:
        os.makedirs(savePath)
    #part 2  根据内页获取图片 
    for j in items:
        insideUrl = "xxxxxx/forum/" + j
        print('.',end='')
        try:
            imgUrl = getImg(insideUrl)
            res=requests.get(imgUrl)
            with open('/Users/fire/A/workshop/pachong/sis/result/%s/%s.jpg' % (i,j),'wb') as f:
                f.write(res.content)
        except:
            continue

print('Done.')
