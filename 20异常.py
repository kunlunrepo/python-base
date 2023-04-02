#
# try:
#     a=eval(input('请输入一个整数:'))
#     b=eval(input('请输入另一个整数：'))
#     z=a/b
#     print(f'{a}/{b}={a/b}')
# except Exception as e:
#     print('出现异常时，所要执行的代码')
#     print(e)
# finally:
#     print('程序执行结束')
#
#
#
# try:
#     a=eval(input('请输入一个整数:'))
#     b=eval(input('请输入另一个整数：'))
#     z=a/b
#     print(f'{a}/{b}={a/b}')
# except Exception as e:
#     print('出现异常时，所要执行的代码')
#     print(e)
# else:
#     print('程序未报错时执行')


try:
    s=input('请输入一个字符串');
    if len(s)<5:
        raise Exception('出错了')
except Exception as e:
    print(e)
    print(e.args) #输出异常对象的参数值
else:
    print('程序未报错时执行')