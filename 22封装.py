
#权限修饰符 使用__ 表示私有

class Person:

    def __init__(self, gender): #gender局部变量
        #定义属性
       self.__gender = gender

    @property
    def gender(self): # 只读属性
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value!='男' and value != '女':
            print('性别赋值有误')
            self.__gender='男'
        else:
            self.__gender = value

p=Person('男')
# print(f'性别{p.__gender}')

p.gender = '动物'
print(f'性别：{p.gender}')
