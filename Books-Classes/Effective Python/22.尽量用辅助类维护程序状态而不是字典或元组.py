# -*- coding:utf-8 -*-


#python字典可以很好的保存某个对象在其生命周期里的动态内部状态
class SimpleGradebook(object):
    """docstring for SimpleGradebook"""
    def __init__(self): #双下划线是系统定义的，一般用户可以自己重写
        self._grades = {} #单下划线是Python程序员使用类时的约定，表明程序员不希望类的用户直接访问属性。仅仅是一种约定！实际上，实例._变量，可以被访问。
    def add_student(self,name):
        self._grades[name] = []  #用个空列表
    def report_grade(self,name,score):
        self._grades[name].append(score)
    def average_grade(self,name):
        grades = self._grades[name]
        return sum(grades) / len(grades)

book0 = SimpleGradebook()
book0.add_student('Jack')
book0.report_grade('Jack',90)

print book0.average_grade('Jack')
        
#当有更多功能需要添加时就过于复杂了

#############【把嵌套结构重构为类】#################
#collections模块中的namedtuple（具名元组）类型非常适合实现，它能很容易定义出精简而又不可改变的数据类
import collections
Grade = collections.namedtuple('Grade',('score','weight'))#构建时，可以按位置指定或者关键字指定各项，这些字段都可通过属性名访问。注意引号

#科目的类，包含考试成绩
class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self,score,weight):
        self._grades.append(Grade(score,weight))

    def average_grade(self):
        total,total_weight = 0,0
        for grade in self._grades:
            total += grade.score*grade.weight #可通过属性名访问
            total_weight += grade.weight
        return total / total_weight


#学生的类，包含正在学习的课程
class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self,name):
        if name not in self._subjects:
            self._subjects[name] = Subject() #每个键值对中的名字对应一个课程类
        return self._subjects[name]

    def average_grade(self):
        total,count = 0,0
        for subject in self._subjects.values():  #dict.values()可以遍历所有的值，dict.keys()遍历所有的键。记住一定要加括号！
            total += subject.average_grade()
            count += 1
        return total / count


#包含所有学生考试成绩的容器类，以学生名字为键，可动态添加学生
class Gradebook(object):
    def __init__(self):
        self._students = {}
    def student(self,name):
        if name not in self._students:
            self._students[name] = Student() #以学生名为键，对应一个学生实体类为值
        return self._students[name]

#虽然上面这些类的代码量是原来那种的几倍，但是理解容易，且范例代码写起来也更清晰，更易扩展
book = Gradebook()
albert = book.student('Albert Einstein')
math = albert.subject('Math')
math.report_grade(80,0.10)
print albert.average_grade()

'''
namedtuple的局限：
1.无法指定各参数的默认值。
2.其实例的各项属性依然可以通过下标及迭代访问。可能导致其他人以不符合设计者意图的方式使用这些元组，从而使以后很难把它迁移为真正的类。
'''
'''
不要使用包含其他字典的字典，也不要使用过长的元组

若容器中包含简单而又不可变的数据，则可先使用namedtuple来表示，待稍后有需要时再修改为完整的类

保存内部状态的字典如果变得比较复杂，那就应该把这些代码拆解为多个辅助类
'''
