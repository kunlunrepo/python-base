#计算1-100偶数累加和
# i=1
# result=0
# while i <= 100:
#     if i % 2 ==0:
#         result += i
#     i+=1
# print(result)

#break continue
# i=1
# while i <= 5:
#     if i==4:
#         print(f'吃饱了不吃了')
#         # break;
#         continue;
#     print(f'吃了第{i}个苹果')
#     i += 1

#正方形
# j=0
# while j<=4:
#     i=0
#     while i <=4:
#         print('*', end='') #列
#         i+=1
#     print() #换行
#     j+=1

#三角形
# j=0
# while j<=4:
#     i=0
#     while i<=j: #一行输出几个
#         print('*', end='') #列
#         i+=1
#     print() #换行
#     j+=1

#9x9乘法表
# j=1
# while j<=9:
#     i=1
#     while i<=j: #一行输出几个
#         print(f'{i}*{j}={i*j}', end='\t') #列
#         i+=1
#     print() #换行
#     j+=1

#for循环
# str1='itheima'
# for i in str1:
#     print(i)

#while...else 循环正常结束时执行的代码
# i=1
# while i<=5:
#     if i==3:
#         print('这遍说的不真诚')
#         # break
#         i+=1
#         continue
#     print('媳妇儿，我错了')
#     i+=1
# else:
#     print('媳妇原谅我')

#for...else 循环正常结束时执行的代码
str1='itheima'
for i in str1:
    print(i)
else:
    print('循环正常结束之后执行的代码')