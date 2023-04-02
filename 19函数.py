#定义 def 函数名(参数):
print('******函数示例******')
def sum_num(a,b): # 定义
    return a+b

result = sum_num(1,2) # 调用
print(result)

print('******函数说明******')
def sum_num(a,b):
    """求和函数"""
    return a + b

help(sum_num)

print('******函数嵌套******')
def testB():
    print('---testB start---')
    print('testB函数执行的代码')
    print('---testB end---')

def testA():
    print('---testA start---')
    print('testA函数执行的代码')
    testB()
    print('---testA end---')
testA()

print('******函数 作用域******')
a = 100 # 全局变量
def testA():
    print(a)

# def testB():
#     a = 200 # 定义局部变量
#     print(a) # 局部变量200

def testB():
    # global 关键字声明a是全局变量
    global a
    a = 200 # 全局变量
    print(a) # 全局变量200

testA()
testB()
print(f'全局变量a = {a}') # 全局变量 a = 100

print('******函数 参数******')
def user_info(name, age, gender='男'):
    print(f'您的名字是{name},年龄是{age},性别是{gender}')

user_info('TOM', 20, '男') # 位置参数 传递和定义参数的顺序及个数必须一致
user_info('小明', age=20, gender='女') # 关键字参数 通过"键=值"
user_info('小明', age=20) # 缺省参数 只有明确制定时才使用，否则使用默认值

def user_info2(*args): # 包裹位置传递
    print(args)

user_info2('TOM')
user_info2('TOM', 18) # 不定长参数

def user_info3(**args): # 包裹关键字传递
    print(args)

user_info3(name='TOM', age=18) # 不定长参数

print('******函数 拆包和交换变量值******')
def return_num():
    return 100, 200
num1, num2 = return_num()
print(num1)
print(num2)

dict1 = {'name': 'TOM', 'age': 18}
a,b = dict1
print(a)
print(b)

a,b=1,2
a,b=b,a
print(a)
print(b)

print('******函数 引用******')
#值是靠引用来传递的 id() 函数可以判断是否为同一个值的引用
# help(id)
a=1
b=a

print(b)
print(id(a))
print(id(b))

a=2
print(b) # int类型为不可变类型

print('******函数 可变和不可变类型******')
#可变类型 列表、字典、集合
#不可变类型 整型、浮点型、字符串、元组

print('******函数 递归******')
def sum_numbers(num):
    if num == 1:
        return 1
    return num + sum_numbers(num - 1) # 递归出口

sum_result=sum_numbers(3) # 调用函数
print(sum_result) # 最终结果

print('******函数 lambda表达式******')
# 如果一个函数有一个返回值，并且只有一句代码

















