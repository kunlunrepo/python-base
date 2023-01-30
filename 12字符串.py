#定义

#下标
# name='abcdef'
# print(name[1])
# print(name[0])
# print(name[2])

#切片 序列[开始位置下标:结束位置下标:步长] 步长=间隔 当前为1 左闭右开 步长的正负决定截取的方向
# name='abcdefg'
# print(name[2:5:4])
# print(name[2:5])
# print(name[:5:2])
# print(name[1:])
# print(name[:])
# print(name[::2])
# print(name[:-1])
# print(name[-4:-1])
# print(name[::])
# print(name[::-1]) # 反转
# print(name[-1:-4:-1]) # 反转

#常用操作方法
#查找 find 字符串.find(子串，开始位置下标，结束位置下标)  rfind()
# mystr="hello world and itcast and itheima and Python"
# print(mystr.find('and'))
# print(mystr.find('and',15,30))
# print(mystr.find('ands'))

#查找 index 字符串.index(子串，开始位置下标，结束位置下标) rindex()
# mystr="hello world and itcast and itheima and Python"
# print(mystr.index('and'))
# print(mystr.index('and',15,30))
# print(mystr.index('ands'))

#查找 count 字符串.count(子串，开始位置下标，结束位置下标)
# mystr="hello world and itcast and itheima and Python"
# print(mystr.count('and'))
# print(mystr.count('and',15,30))
# print(mystr.count('ands'))

#修改 字符串.replace(旧子串，新子串，替换次数)
# mystr="hello world and itcast and itheima and Python"
# print(mystr.replace('and','he'))
# print(mystr.replace('and','he',10))
# print(mystr)

#修改 字符串.split(分割字符，分割字符出现的次数)
# mystr="hello world and itcast and itheima and Python"
# print(mystr.split('and'))
# print(mystr.split('and',2))
# print(mystr.split(' '))
# print(mystr.split(' ', 2))

#修改 字符串.join(多字符串组成的序列)
# list1=['chuan', 'zhi', 'bo', 'ke']
# t1=('aa','b','cc','ddd')
# print('_'.join(list1))
# print('...'.join(t1))

#修改 字符串.capitalize() 将字符串第一个字符转换成大写
# mystr="hello world and itcast and itheima and Python"
# print(mystr.capitalize())

#修改 字符串.title() 将字符串每个单词首字母转换成大写
# mystr="hello world and itcast and itheima and Python"
# print(mystr.title())

#修改 字符串.lower() 字符串中大写转小写
# mystr="hello world and itcast and itheima and Python"
# print(mystr.lower())

#修改 字符串.upper() 字符串中小写转大写
# mystr="hello world and itcast and itheima and Python"
# print(mystr.upper())

#修改 字符串.lstrip() 删除字符串左侧空白字符
# mystr="  hello world and itcast and itheima and Python"
# print(mystr.lstrip())

#修改 字符串.rstrip() 删除字符串右侧空白字符
# mystr="hello world and itcast and itheima and Python    "
# print(mystr.rstrip())

#修改 字符串.strip() 删除字符串两侧空白字符
# mystr="   hello world and itcast and itheima and Python    "
# print(mystr.strip())

#修改 字符串.ljust(长度，填充字符) 返回字符串左对齐，并使用指定字符串填充至对应长度的新字符串
# mystr="hello"
# print(mystr.ljust(10, '.'))

#修改 字符串.rjust(长度，填充字符) 返回字符串右对齐，并使用指定字符串填充至对应长度的新字符串
# mystr="hello"
# print(mystr.rjust(10, '.'))

#修改 字符串.center(长度，填充字符) 返回字符串居中，并使用指定字符串填充至对应长度的新字符串
# mystr="hello"
# print(mystr.center(10, '.'))

#判断 字符串.startswith(字符串，开始位置下标，结束位置下标) 检查字符串是否以指定字符串开头
# mystr="hello world and itcast and itheima and Python"
# print(mystr.startswith('hello'))
# print(mystr.startswith('hello', 5, 20))

#判断 字符串.endswith(字符串，开始位置下标，结束位置下标) 检查字符串是否以指定字符串结尾
# mystr="hello world and itcast and itheima and Python"
# print(mystr.endswith('Python'))
# print(mystr.endswith('Python', 5, 20))

#判断 字符串.isalpha() 如果字符串至少有一个字符并且所有字符都是字母则返回true
# mystr1='hello'
# mystr2='hello12345'
#
# print(mystr1.isalpha())
# print(mystr2.isalpha())

#判断 字符串.isalpha() 如果字符串只包含数字则返回true
# mystr1='aaa12345'
# mystr2='12345'
#
# print(mystr1.isdigit())
# print(mystr2.isdigit())

#判断 字符串.isalnum() 如果字符串至少有一个字符并且所有字符都是字母或数字则返回true
# mystr1='aaa12345'
# mystr2='12345-'
#
# print(mystr1.isalnum())
# print(mystr2.isalnum())

#判断 字符串.isspace() 如果字符串只包含空白则返回true
mystr1='1 2 3 4 5'
mystr2='  '

print(mystr1.isspace())
print(mystr2.isspace())




