#learn ast
'''
>>> import ast
>>> ast.parse
<function parse at 0x1032ce378>
>>> ast.parse("x=2")
<_ast.Module object at 0x1032c67b8>
>>> ast.dump(ast.parse("x=2"))
"Module(body=[Assign(targets=[Name(id='x', ctx=Store())], value=Num(n=2))])"
>>>

但是不同python版本之间的抽象语法树都有不同。

Hy编程语言为python创造一种新的语法，并将其解析并编译成标准的python抽象语法树。
它是LISP的一个变种。 
'''