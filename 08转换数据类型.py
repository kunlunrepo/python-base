#float
num1=1
print(float(num1))
print(type(float(num1)))

#str
num2=10
print(type(str(num2)))

#tuple 列表->元组
list1=[10,20,30]
print(tuple(list1))
print(type(tuple(list1)))

#list 元组->列表
t1=(100,200,300)
print(list(t1))
print(type(list(t1)))

#eval 将字符串中的数据转换成python表达式原本的数据类型
str1='10'
str2='[1,2,3]'
str3='(1000,2000,3000)'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))