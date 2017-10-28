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