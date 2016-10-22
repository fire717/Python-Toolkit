#不知道为什么直接导入整个TXT文档不行（虽然原文本应该也只有一行，不然还要处理换行问题），换成一行行操作就可以了，待解决
#需求来源于从知乎上复制几个回答想要收藏整理到TXT里然后放到自己的kindle上，首先是无法复制，直接查看源码，然后全是<br>标签，于是写了个这个替换成空行了。

text_old = open('1.txt','r')
text_new = open('2.txt','w')
for line in text_old.readlines():
    s= line.replace('<br>','\n')
    text_new.writelines(s)
    
text_old.close()
text_new.close()

print ('Success!')
input()
