### 常用
* 合并
```
x1 = np.array([[1,2]])
x2 = np.array([[3,4]])
np.concatenate((x1,x2),axis=0)  # 默认情况下，axis=0可以不写
>>array([[1, 2],
       [3, 4]])
```

* 众数
```
a = np.array([1,2,3,1,2,1,1,1,3,2,2,1])
counts = np.bincount(a)
#bin的数量比x中的最大值大1，每个bin给出了它的索引值在x中出现的次数
#>>array([0, 6, 4, 2], dtype=int64)
np.argmax(counts)
#>> 1
```
