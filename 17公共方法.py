# 运算符 +、in、not in
str1 = 'aacc'
str2 = 'bb'

list1 = [1,2]
list2 = [10,20]

t1 = (1,2)
t2 = (10,20)

dict1 = {'name': 'Python'}
dict2 = {'age': 30}

# + 合并 字符串、列表、元祖
# print(str1+str2)
# print(list1+list2)
# print(t1+t2)

# * 复制 字符串、列表、元祖
# print(str1*2)
# print(list1*2)
# print(t1*2)

# in 合并 字符串、列表、元祖、字典
# print('c' in str1)
# print(1 in list1)
# print(3 in t1)
# print('name' in dict1) # 判断key
# print({'name': 'Python'} in dict1)

# not in 合并 字符串、列表、元祖、字典
# print('c' not in str1)
# print(1 not in list1)
# print(3 not in t1)
# print('name' not in dict1) # 判断key

# len() 元素个数
# print(len(str1))
# print(len(list1))
# print(len(t1))
# print(len(dict1))

# del del() 删除
# del str1
# print(str1)
# del list1
# print(list1)
# del t1
# print(t1)
# del dict1
# print(dict1)

# max min
# print(max(str1, str2)) # ASCII
# print(max(list1))
# print(max(list1, list2))
# print(max(t1, t2))
# print(max(dict1, dict2)) # 不存在

# rang() 生成start到end的数字，步长为step
# for i in range(1, 10, 1):
#     print(i)
# print(range(1, 10, 1)) #不包含end step默认1
# for i in range(10): # 0开始
#     print(i)

# enumerate 将一个可遍历的数据对象组合为一个索引序列,同时列出数据和数据下标，一般用在for循环中
# for index, value in enumerate(['a','b','c','d','e','f']):
#     print(index,value)
# for index, value in enumerate(['a','b','c','d','e','f'], 1):
#     print(index,value)

# 容器数据类型转换
# tuple() 转元组
# print(tuple([10, 20, 30, 20, 40, 50]))
# print(tuple({100,300,200,500}))

# list() 转列表
# print(list({100,300,200,500}))
# print(list(('a','b', 'c','d', 'e', 'f')))

# set() 转集合
print(set([10, 20, 30, 20, 40, 50]))
print(set(('a','b', 'c','d', 'e', 'f')))

# {}=set []=list ()=tuple