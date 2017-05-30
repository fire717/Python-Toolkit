####15年实习时写的，只是现在来看就觉得的确太烂了，甚至都没有模块化处理，毕竟那时候连PYTHON都没接触过，留念留念。= =
--------------------------------------------------------------------------------------------------------------------
#-*- coding: gbk -*-  
import urllib
import os
import re
import urllib2
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#输入关键词得到百度搜索页面
keyword=raw_input("请输入关键词：\n")
print("收到关键词为"+str(keyword)+"，开始工作！")

#@@@获取所有搜索到的网页链接
#伪装浏览器
headers = {  
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
}  
req = urllib2.Request(  
    url = "https://www.baidu.com/s?wd="+keyword,  
    headers = headers  
)
	#判断搜索结果链接
response = urllib2.urlopen(req)
html = response.read()
links= re.findall('"http://www.baidu.com/link\?url=.*?"',html)
links2=list(set(links))

for x in links2:
	link_true=x.strip('\"')
	html_1 = urllib2.urlopen(link_true).read()
	#获取网页字符集
	charset1=re.findall(u'(?<=charset=)[^\"]*(?=\")',html_1)
	str_charset1=''.join(charset1)
	if str_charset1=='':
		continue

	#获取关键词
		links= re.findall('(?<=meta name=\"\weywords\" content=\").+?(?=\")',html_1)
		str_links=''.join(links)
		ch_links=str_links.decode(str_charset1)

		keys1=ch_links.split(" ")
		keys2=list(set(keys1))
	#拆分关键词，判断 
		for i in keys2:
			if i==keyword.decode('gbk'):
		#存储名称和链接到数据库
				conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="db_test",charset="utf8") 
				cursor = conn.cursor()  
		#写入    
				name1=re.findall(u'(?<=\<title\>).+?(?=\<\/title)',html_1)
				str_name=''.join(name1)
				ch_name=str_name.decode(str_charset1)
				
				sql = "insert into company(name,url) values(%s,%s)"   
				param = (ch_name,link_true)    
				n = cursor.execute(sql,param)    
				print 'insert',n    
   
				conn.commit()
				conn.close()   
				break
