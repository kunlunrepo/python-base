
print('hello python')

age=18
# print(age)

#格式化输出
'''

\n
\t
'''

age=18
name='TOM'
weight=75.5
student_id=1

print('我的名字是%s' % name)
print('我的学号是%4d' % student_id)
print('我的体重是%.2f' % weight)
print('我的名字是%s, 今年%d岁了' % (name, age))
print('我的名字是%s岁， 明年%d岁了' % (name, age+1))
print(f'我的名字岁{name},明年{age+1}岁了')