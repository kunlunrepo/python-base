
#文件的打开
# file=open('./a.txt', 'w', encoding='utf-8')
#
# #使用覆盖写模块，写入helloworld
# file.write('hello world')
# file.write('\n')
# file.close()
#
#
# file=open('./a.txt', 'a', encoding='utf-8')
# lst=['2023',  '新年快乐'] #要求写入的是string
# file.writelines(lst)
# file.close()


#文件的读取
# file=open('./a.txt','r', encoding='utf-8')
# s=file.read()
# print(type(s))
# print(s)
# file.close()
#
# file=open('./a.txt','r', encoding='utf-8')
# line=file.readline()
# print('*'*40)
# print(type(line))
# print(line)
# # file.close()
#
# lst=file.readlines()
# print('*'*40)
# print(type(lst))
# print(lst)
# file.close()


#文件的复制
with open('./a.txt','rb') as srcFile:
    with open('./b.txt', 'wb') as targetFile:
        targetFile.write(srcFile.read())