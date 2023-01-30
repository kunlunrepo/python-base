#定义
t1=(10,20,30)
t2=(10,) #必须添加,

#查找 下标
tuple1=('aa','bb','cc','bb')
print(tuple1[0])

#查找 元组.index(数据) 如果数据存在返回对应的下标，否则报错
print(tuple1.index('aa'))

#查找 count()
print(tuple1.count('bb'))

#查找 len() 统计元组中数据的个数
print(len(tuple1))

#注意：元组是不能修改的，但是元组中存在的列表的，列表是可以修改的