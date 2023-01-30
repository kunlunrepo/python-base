#定义
dict1 = {'name': 'Tome', 'age': 20, 'gender': '男'}
dict2 = {}
dict3 = dict()

# print(dict1)
# print(dict2)
# print(type(dict3))

#新增
# dict1['name'] = "Rose"
# print(dict1)

#删除
# del(dict1)
# del dict1['name']
# dict1.clear()
# print(dict1)

#修改
# dict1['name'] = 'lili'
# print(dict1)

#查找
# print(dict1['name']) # 不存在key会报错
# print(dict1.get('id', '123')) #不传默认值返回none
#
# print(dict1.keys()) #返回可迭代对象 for循环可以遍历
# for key in dict1.keys():
#     print(dict1[key])
# print(dict1.values())
# for value in dict1.values():
#     print(value)
# print(dict1.items())
# for key,value in dict1.items():
#     print(key)