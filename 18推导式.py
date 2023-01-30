# 定义 化简代码 用一个表达式创建一个有规律的列表或控制一个一规律列表 列表[]、字典{}、集合{}
list1=[]

# while循环
# i=0
# while i < 10:
#     list1.append(i)
#     i+=1
# print(list1)

# for循环
# for i in range(10):
#     list1.append(i)
# print(list1)

# ☆列表推导式
# list1 = [i for i in range(10)] # for前面的是返回值
# print(list1)

# 带if的列表推导式
# list1 = [i for i in range(0, 10, 2)]
# print(list1)
# list1 = [i for i in range(10) if i % 2 == 0]
# print(list1)

# 多个for循环实现列表推导式 嵌套循环
# list1 = [(i,j) for i in range(1,7) if i % 2 == 0 for j in range(3)] # [(2, 0), (2, 1), (2, 2), (4, 0), (4, 1), (4, 2), (6, 0), (6, 1), (6, 2)]
# print(list1)

# ☆字典推导式 快速合并列表为字典或提取字典中目标数据
# dict1 = { i:i**2 for i in range(10)}
# print(dict1)Ï

# list1=['name','age', 'class']
# list2=['Tom', 20]
#
# dict1 = { list1[i]:list2[i] for i in range(len(list2) if len(list1)>len(list2) else len(list1)) } # 列表数据不一样报错
# print(dict1)

# 提取字典中目标数据
# conuts = {'MBP': 268, 'HP':125}
# count1 = { k:v for k,v  in conuts.items() if v >= 200}
# print(count1)

# ☆集合推导式
set1 = {i**2 for i in [1,1,2]} #
print(set1)