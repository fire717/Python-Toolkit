### 常用

* 修改数据类型
```
x = np.array(x,dtype=np.int32)
```

* one-hot
```
num_classes = 10
arr = [1,3,4,5,9]
arr = np.eye(10)[arr]
```

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

* 交换两行/列
```
#（例如opencv读取图片为RGB的顺序，想转位BGR）
img = cv2.imread("xx.jpg") #img.shape = h*w*3
img[:,:,[0,2]] = img[:,:,[2,0]]  #交换了第三维中的0列和2列 即BGR转为RGB
```

* 求偏度、峰度

```
R = np.array([1, 2, 3, 4, 5, 6]) #初始化一组数据
R_mean = np.mean(R) #计算均值
R_var = np.var(R)  #计算方差
R_sc = np.mean(((R - R_mean)/R_var**0.5) ** 3) #计算偏斜度
R_ku = np.mean((R - R_mean) ** 4) / pow(R_var, 2) #计算峰度
print([R_mean, R_var, R_sc, R_ku])
```

* 二维数组按列或者行求和
```
def non_zero_mean(np_arr):
    exist = (np_arr != 0)
    num = np_arr.sum(axis=1)
    #行为0列为1
    den = exist.sum(axis=1)
    return num/den

```

### 工具
* [打乱训练集和验证集](./tools/transformation_data.py)
* [计算图像数据集均值标准差](./tools/compute_imgs_mean_std.py)
