%matplotlib inline
import matplotlib.pyplot as plt # 导入绘图包
labels = 'frog', 'hogs', 'dogs', 'logs' # 设定数据标签
sizes = 15, 20, 45, 10 # 设定数据
colors = 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral' # 设定颜色
explode = 0, 0.1, 0, 0
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
plt.axis('equal')
plt.show()
