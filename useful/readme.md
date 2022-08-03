* 新建文件夹

```python
if not os.path.exists(feature_dir):
    os.makedirs(feature_dir)
```

* 后台运行并保存log

```python

nohup python -u test.py > test.log 2>&1 &
#最后的&表示后台运行
#2 输出错误信息到提示符窗口
#1 表示输出信息到提示符窗口, 1前面的&注意添加, 否则还会创建一个名为1的文件
#最后会把日志文件输出到test.log文件

#查看
tail -f test.log#如果要实时查看日志文件使用命令
cat test.log#查看全部输出使用命令
```

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
    json.dump(x, f, ensure_ascii=False)   #单行
print('done')
## 格式化
with open(r"result.json", 'w') as f:  
    json.dump(res, f, ensure_ascii=False, indent=4)  

#read
with open(r"./x.json",'r') as f:
    x = json.loads(f.readlines()[0])  
#读取格式化后的多行json
with open(r"./x.json",'r') as f:
    x = json.load(f)

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

* timestamp 转换标准时间
```python
# 把时间处理 以找到登陆时间
import time
def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
 # value为传入的值为时间戳(整形)，如：1332888820
    value = time.localtime(value)
 ## 经过localtime转换后变成
 ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
 # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(format, value)
    return dt
def datetime_timestamp(dt):
  #dt为字符串
  #中间过程，一般都需要将字符串转化为时间数组
    time.strptime(dt, '%Y-%m-%d %H:%M:%S')
  ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
  #将"2012-03-28 06:53:40"转化为时间戳
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return int(s)

d = datetime_timestamp('2015-03-30 16:38:20')
print(d)
s = timestamp_datetime(1427704700)
print(s)
```

* 排序
```python
#方法1.用List的成员函数sort进行排序，在本地进行排序，不返回副本
#方法2.用built-in函数sorted进行排序（从2.4开始），返回副本，原始输入不变
listX = [[1,4],[2,5],[3,3]]
sorted(listX, key=lambda x : x[1])
#>>[[3, 3], [1, 4], [2, 5]]

### 两个list按同意顺序排序
list1 = [1, 2, 3, 4, 15, 6]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
c = list(zip(list1,list2))
c.sort(reverse=True) #降序du
list1[:],list2[:] = zip(*c)
print(list1,list2)
```

* 文件路径获取
```python
path1 = os.getcwd()   #最外层执行的main.py的路径
path2 = os.path.dirname(os.path.realpath(__file__))  #当前py文件的绝对路径
```

* 同一行刷新打印
```python
print("\r",object,end="",flush=True)
 
#e.g.
for i,img_name in enumerate(img_names):
    print("\r",str(i)+"/"+str(len(img_names)),end="",flush=True)
```

* PIL resize比opencv更清晰
```
img = cv2.imread("000000000113_0.jpg")
img = Image.fromarray(img)
img = img.resize((192,192))
img = np.array(img)
```

* base64转opencv
```
def bs64toimg(bs64):

    img_b64decode = base64.b64decode(bs64)  # base64解码
     
    img_array = np.fromstring(img_b64decode,np.uint8) # 转换np序列
    img=cv2.imdecode(img_array,cv2.COLOR_BGR2RGB)  # 转换Opencv格式

    return img

```
