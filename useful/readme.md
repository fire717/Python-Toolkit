* 文件读取

```python
###1.python  
#读写txt
with open(r'./data/user_dict.txt','r',encoding='utf-8') as f:
    data = f.readlines()
#追加模式
with open(r'./data/user_dict.txt','a',encoding='utf-8') as f:
    t = '你好'
    f.write('\n'+t)

#按行读取tsv / 内存大可以直接.readlines()
with open('./data/train.tsv',encoding = 'utf-8') as file:
    line = file.readline()
    limit = 0
    while line and limit<10:
        print(line)
        limit+=1
        line = file.readline()

###2.json 存储dict
x = {..}
#save
with open(r"./x.json",'w') as f:  
    json.dump(x, f, ensure_ascii=False)     
print('done')
#read
with open(r"./x.json",'r') as f:
    for line in f:
        x = json.loads(line)  

###3.numpy 存储list
x = [x,]
np.save("./././x.npy",x)
x = np.load(r"./././x.npy")

###4.pandas
#read xlsx
data = pd.read_excel(r'xxxx.xlsx','Sheet1')

#dict to df
result = {x:1,y:2,..}  
df = pd.DataFrame(list(result.items()), columns=['key','value'])
#save df
df.to_csv(r"./result.csv", index=False,header=True)
#read
df = pd.read_csv(r'./result.csv',encoding = 'gbk')
```

* 字符串判断

```pyhton
s.islower() #判断是否所有字符小写
s.isupper() #判断是否所有字符大写
s.isalpha() #判断是否所有字符为字母
s.isalnum() #判断是否所有字符为字母或数字
s.isdigit() #判断是否所有字符为数字
s.istitle() #判断是否所有字符为首字母大写
```

* 统计list元素出现次数

```PYHTON
from collections import Counter
x = [1,2,3,2]
y= '1232'
Counter(x)
#>>Counter({2: 2, 1: 1, 3: 1})  #就是一个dict
Counter(y)
#>>Counter({'2': 2, '1': 1, '3': 1})
Counter('1232')['2']
#>>2
```
