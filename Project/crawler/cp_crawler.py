#coding = utf-8
#Fire / 2018.6.30
import requests
from bs4 import BeautifulSoup as bs
import re
import time
 
 
def spider(url, headers):
    r = requests.get(url=url, headers=headers)
    r.encoding = 'gb2312'
    html = r.text
    with open('t.html','w',encoding='utf-8') as f:
        f.write(html)

    # 解析html
    soup = bs(html, 'lxml')

    ul = soup.find_all(name='tr',attrs={'class': 't_tr1'})
    print(len(ul))
    f = open('history3D.txt','w')
    for i in range(len(ul)):
        date = str(ul[i].find_next(name='td'))[4:11]
        number = str(ul[i].find_next(name='td',attrs={'class': 'cfont2'})).split('>')[1][:5]
        f.write(date+':'+number+' '+'\n')

    f.close()
    print('done!')
 

 
if __name__ == '__main__':
 
    url = "https://datachart.500.com/sd/history/inc/history.php?limit=18173&start=2000000&end=2018173"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'datachart.500.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    spider(url, headers)

