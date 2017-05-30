#coding=utf-8
import urllib
import re
import os
import urllib2

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getTitle(html):
    reg = r'<h4>\n(.*)</h4>'
    urlre = re.compile(reg)
    title = re.findall(urlre,html)
    return title

i = 10  #索引页

while i<100:
    raw_url = "http://wufazhuce.com/question/%s" % i
    html = getHtml(raw_url)
    print i,':',getTitle(html)[0].strip()
    i+=1
