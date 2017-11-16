* 合并两个df
```
np.concatenate((x,y),axis=0)
```

* 判断是否nan
```
if row['xxx'] is np.nan:
```

* 获取某列值等于某个值的行
```
df[df['列名'].isin([相应的值])]
```

* 重新从0开始索引
```
df.reset_index(drop=True)  
```
