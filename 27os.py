
import os

print('当前工作路径', os.getcwd())

print('获取指定路径下的所有文件或文件夹的名称', os.listdir()) #当前路径

print('获取指定路径下的所有文件或文件夹的名称', os.listdir('./mypkg')) #指定路径

# os.mkdir(os.getcwd()+'/aa') #路径的拼接
# os.makedirs('./xx/yy/zz') # 创建多级文件夹

# os.rmdir('./aa')
# os.removedirs('./xx/yy/zz')

# os.chdir('./mypkg') # 切换当前文件运行路径
# print('当前工作路径', os.getcwd())
# print(os.listdir())

# os.remove('./b.txt')

import os.path

print('文件或目录的绝对路径', os.path.abspath('a.txt'))

print('文件或目录是否存在', os.path.exists('a.txt'))

#拼接路径
print('拼接路径', os.path.join(r'D:\personal\code-repo\hm\python-base','b.txt'))

#分隔文件名和扩展名
print(os.path.splitext('b.txt'))
print("获取文件的名称", os.path.basename(r'D:\personal\code-repo\hm\python-base\b.txt'))
print("获取文件的路径", os.path.dirname(r'D:\personal\code-repo\hm\python-base\b.txt'))

# r 原字符 使转义字符失效

print("判断是否是目录", os.path.isdir(r'D:\personal\code-repo\hm\python-base'))