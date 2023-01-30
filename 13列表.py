#格式 [数据1,数据2,数据3,数据4]

#查找 下标
# name_list=['Tom','Lily','Rose']
# print(name_list[0])
# print(name_list[1])
# print(name_list[2])

#查找 列表.index(数据，开始位置下标，结束位置下标) 返回指定数据所在位置的下标
# name_list=['Tom','Lily','Rose']
# print(name_list.index('Lily', 0, 2))

#查找 count() 统计指定数据在当前列表中出现的次数
# name_list=['Tom','Lily','Rose']
# print(name_list.count('Lily'))

#查找 len() 列表长度 列表中数据的个数
# name_list=['Tom','Lily','Rose']
# print(len(name_list))

#查找 in 判断指定数据在某个列表序列
# name_list=['Tom','Lily','Rose']
# print('Lily' in name_list)
# print('Lilys' in name_list)

#查找 not in 判断指定数据不在某个列表序列
# name_list=['Tom','Lily','Rose']
# print('Lily' not in name_list)
# print('Lilys' not in name_list)

#增加 列表.append(数据) 列表结尾追加数据
# name_list=['Tom','Lily','Rose']
# # name_list.append('xiaoming')
# name_list.append(['xiaoming', 'xiaohong']) # 追加整个序列到列表
# print(name_list)

#增加 列表.extend(数据) 列表结尾追加数据 如果数据是一个序列，则将这个序列的数据逐一添加到列表
# name_list=['Tom','Lily','Rose']
# # name_list.extend('xiaoming')
# name_list.extend(['xiaoming','xiaohong'])
# print(name_list)

#增加 列表.insert(位置下标，数据)
# name_list=['Tom','Lily','Rose']
# name_list.insert(1, 'xiaoming')
# print(name_list)

#删除 del 目标
# name_list=['Tom','Lily','Rose']
# # del name_list #报错
# del name_list[0] #删除指定数据
# print(name_list)

#删除 列表.pop(下标) 删除指定下标的数据(默认为最后以一个)，并返回该数据
# name_list=['Tom','Lily','Rose']
# del_name=name_list.pop(1)
# print(del_name)
# print(name_list)

#删除 列表.remove(数据) 移除列表中某个数据的第一个匹配项
# name_list=['Tom','Lily','Rose']
# name_list.remove('Rose')
# print(name_list)

#删除 clear() 清空列表
# name_list=['Tom','Lily','Rose']
# name_list.clear()
# print(name_list)

#修改 修改指定下标数据
# name_list=['Tom','Lily','Rose']
# name_list[0]='aaa'
# print(name_list)

#修改 reverse() 逆置
# name_list=['Tom','Lily','Rose']
# name_list.reverse()
# print(name_list)

#修改 列表.sort(key=None，reverse=False) 排序
# num_list=[1,5,2,3,6,8]
# num_list.sort()
# print(num_list)

#复制
# name_list=['Tom','Lily','Rose']
# name_li2=name_list.copy()
# print(name_li2)

#列表的循环遍历 while
# name_list=['Tom','Lily','Rose']
# i=0
# while i<len(name_list):
#     print(name_list[i])
#     i+=1

#列表的循环遍历 for
# name_list=['Tom','Lily','Rose']
# for i in name_list:
#     print(i)

#列表嵌套
name_list=[['小明','小红','小绿'],['Tom','Lily','Rose']]
print(name_list)