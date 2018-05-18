#learn generator

def MyGenerator():  
    print('sss')
    value = (yield 1)
    print('he')  
    print(value)
    value = (yield value)  
  
  
gen = MyGenerator()  
print(next(gen))
print('---')
print(gen.send(2))  
#print(gen.send(3))  

'''
sss
1
---
he
2
2
[Finished in 0.2s]
'''
