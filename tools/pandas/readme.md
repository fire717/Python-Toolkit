* 根据index和head赋值
```
df.loc['0','A'] = 1
```

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

* 去掉重复值
```
df['xx'].drop_duplicates()
```

* 排序
```
df = df.sort_values(["xx"])
```
