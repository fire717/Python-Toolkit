## 常用命令


* ps -ef|grep xxx                        查看xxx用户下的进程
* nohup python train.py > train.out 2>&1 &          后台运行脚本，然后tail -f yy.out 实时打印显示
* [Linux统计文件夹、文件数量的命令](https://www.cnblogs.com/uzipi/p/6100790.html)
```shell
# 查看当前目录下的文件数量（不包含子目录中的文件）
ls -l|grep "^-"| wc -l

# 查看当前目录下的文件数量（包含子目录中的文件） 注意：R，代表子目录
ls -lR|grep "^-"| wc -l

# 查看当前目录下的文件夹目录个数（不包含子目录中的目录），同上述理，如果需要查看子目录的，加上R
ls -l|grep "^d"| wc -l

# 查询当前路径下的指定前缀名的目录下的所有文件数量
# 例如：统计所有以“20161124”开头的目录下的全部文件数量
ls -lR 20161124*/|grep "^-"| wc -l
```
