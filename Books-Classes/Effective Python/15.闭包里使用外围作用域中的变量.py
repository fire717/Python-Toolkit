#对list排序，但是要把出现在某个列表中的数字排在其他数字之前


def sort_priority(values,group):
    def helper(x):
        if x in group:
            return (0,x)
        return (1,x)
    values.sort(key=helper)

numbers = [8,3,1,2,5]
group = {2,3,5}
sort_priority(numbers,group)
print(numbers)
#>>[2, 3, 5, 1, 8]
'''
python支持闭包（closure）：闭包是一种定义在某个作用域中的函数，它引用了那个作用域里的变量。
helper之所以能访问sort_priority的group参数，原因在于它是闭包

python函数是一级对象，即可直接引用函数、把函数赋给变量、把函数当成参数传给其他参数，并通过表达式及if语句对其进行比较和判断。
所以这里可以把helper这个闭包函数传给sort的key参数

python使用特殊的规则比较两个元组。首先比较各元组中下标为0的对应元素，如果相等，再比较下标为1 的对应元素...以此类推
'''

##########获取闭包内的数据
###【python3】###
#nonlocal语句的意思是在给相关变量赋值时应在上层作用域中查找该变量 / 唯一限制在于不能延伸到模块级别，防止污染全局作用域
#与global相对
def sort_priority3(numbers,group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True  #表示是否出现了优先级更高的元素。使函数调用者能够做出相应处理
            return (0,x)
        return (1,x)
    numbers.sort(key=helper)
    return found
    #为了防止滥用，只推荐在很简单的函数里使用nonlocal


###【python2】###
#py2中没有nonlocal关键字。
#可利用python作用域规则来实现。虽然不太优雅，但已成了一种python编程习惯。
#即使用可变值，比如包含单个元素的list
#但是...当我把found当成普通变量测试时（去掉[]），发现结果也对啊....
#再把group由dict换成list...结果也对...
def sort_priority2(numbers,group):
    found = [False]
    def helper(x):
        if x in group:
            found[0] = True
            return (0,x)
        return (1,x)
    numbers.sort(key=helper)
    return found[0]

#好吧上面两个问题暂时是想不通了
#百度下压压惊
#[Python 五个知识点搞定作用域](http://python.jobbole.com/86465/)
#终极版作用域
name = "lzl"
def f1():
    print(name)
def f2():
    name = "eric"
    f1()
f2()
# 输出：lzl
#这里本身的解释很简短，一头雾水
### 我觉得因为f1是在f2之外声明的，所以它的上层就是全局变量，不会从f2里找。
#把f1声明放进f2中后，输出的就是eric了。
#就是说，f2只是调用了一下f1，f1还是在f2外层执行的（如果这里把name当成参数传进去就不一样了）
#测试了下在f1中声明了global了一个全局变量，但是f2中还是不能引用，也不知道这能不能解释
#那么在这里的意思就是，函数内部找不到变量时，会从定义时的上层去找，而不是调用时。这是自己观察出来的，期待后面研究其他书得到印证。


#新浪面试题
li = [lambda :x for x in range(10)]
print(type(li))
print(type(li[0]))
# <class 'list'>
# <class 'function'>

res = li[0]()
print(res)
#输出：9
#函数在没有执行前，内部代码不执行
#因为x最后循环成了9，所以每一个return x出来的值都是9
'''
Python中是没有块级作用域的，代码块里的变量，外部可以调用；
即使执行了一下函数，name的作用域也只是在函数内部，外部依然无法进行调用
'''
##【关于函数名】##
'''
假如定义了函数f1()
那么访问f1()，就会得到f1()中的返回值
访问f1,就会得到f1函数的内存地址
'''
