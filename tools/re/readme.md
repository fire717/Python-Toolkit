* 搜索

```python
#[\u4e00-\u9fa5]匹配中文，[^\u4e00-\u9fa5]匹配非中文
#py2
t = re.compile(r'[\u4e00-\u9fa5]')
re.search(t,text)

#py3
ch = re.compile(u'[\u4e00-\u9fa5]+')
words = ch.search(line.strip())
word = words.group()
```

* 分割

```python
t = re.compile(r'[。，;；、]')
sent_list = t.split(text)
```

* 替换

```python
t = re.compile(r'[。，;；、]')
replacedStr = re.sub(t, "222", text)
```
