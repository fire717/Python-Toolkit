# Python-Toolkit

Python常用代码、轮子。

* [一般常用功能](./useful)


### 库&框架
* 图像处理： [OpenCV](./tools/OpenCV) | [Pillow(PIL)](https://www.osgeo.cn/pillow/)
* 数据处理： [Numpy](./tools/numpy) | [Pandas](./tools/pandas)
* 可视分析： [matplotlib](./tools/matplotlib) | [seaborn](./tools/seaborn)
* 文字处理： [re](./tools/re)
* 后端： [Flask（中文文档）](https://dormousehole.readthedocs.io/) | [FastAPI（官方文档）](https://fastapi.tiangolo.com/)
* 其他：     [jupyer notebook](./tools/jupyter)

### 书&课程
* [《Effective Python 编写高质量Python代码的59个有效方法》](/Books-Classes/Effective-Python)
* 《Python高手之路》:  [装饰器](./Books-Classes/PythonHackersGuide/learn_decorator.ipynb) | [迭代器send](./Books-Classes/PythonHackersGuide/learn_generator_send.py) | [抽象语法树](./Books-Classes/PythonHackersGuide/ast.py) |[memoization](https://blog.csdn.net/feeltouch/article/details/45072725) | [multiprocessing](https://blog.csdn.net/cityzenoldwang/article/details/78584175)
* [《Python Parallel Programming Cookbook》中文版](https://github.com/laixintao/python-parallel-programming-cookbook-cn)

### 性能探索
* [多进程加速for循环](./speed/multiprocessing_for.py)

### 小工具
* [文件夹下图片批量重命名](./tools/mine/rename.py)
* [批量复制图片](./tools/mine/copyImg.py)
* [批量移动图片](./tools/mine/moveImg.py)
* [根据文件大小筛选文件夹下的文件](./tools/mine/filterSize.py)
* [8UC1_8UC3_YUV420sp_RGB图片互相转换](./tools/OpenCV/imgTransfer.py)
* [图片拼接pdf](./tools/mine/img_to_pdf.py)

### 小项目
* [【爬虫们】](/Project/crawler) 
* [手机远程控制电脑](/Project/Remote-Control-Computer) 
* [彩票号码生成](/Project/CaiPiao)
* [图片转字符图片](/Project/pic2charpic)
* [微信图灵机器人](/Project/wechatRobot)
* [微信生命线游戏](/Project/Lifeline)
* [模拟50胜率盒子策略](/Project/half_win_box.py)

### 代码片段
* [抽象类](/CodePiece/abstract.py)
* [统计函数运行时间装饰器](/CodePiece/timecost.py)
* [求平方根](/CodePiece/squareroot.py)
* [批量替换文本中字符](/CodePiece/%E6%89%B9%E9%87%8F%E6%9B%BF%E6%8D%A2%E6%96%87%E6%9C%AC%E4%B8%AD%E7%9A%84%E5%AD%97%E7%AC%A6.py)
* [投骰子123我赢45你赢6重投](/CodePiece/投骰子123我赢45你赢.py)
* [解压MNIST数据集](/CodePiece/unzip_MNIST.py)
* [二值图转3通道](/CodePiece/gray2rgb.py)


## 【扩展】：Linux

#### 0.Linux通过python3的print中文报错
```shell
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

#### 1.[命令行常用指令](./linux/)

#### 2.shell脚本
* [获取文件夹下所有文件名](./linux/shell/getAllName.sh)

#### 3.C++
* [常用功能工具函数封装 fire_utils.h](././CodePiece/cpp/fire_utils.h)
* [vector排序索引](./CodePiece/cpp/sort_index.cpp)
