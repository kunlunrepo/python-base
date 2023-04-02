
# 只要具有相同的方法就可以实现多态

class Dog():
    def speak(self):
        print('小狗说话：旺')
        
class Frog():
    def speak(self):
        print("青蛙说话：呱")


class Cat():
    def speak(self):
        print("小猫说话：喵喵")
        
        
def fun(x): #x的数据类型是什么
    x.speak()
    
c=Cat()
d=Dog()
f=Frog()

import random
lst=[c,d,f]

for i in range(10):
    x=random.choice(lst)
    fun(x)
    print("*"*30)