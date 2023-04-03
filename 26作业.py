
file=open('b.txt', 'r', encoding='gbk')
ticket_price=file.read()
#字符串处理
ticket_price=eval(ticket_price.split('=')[1]) #对象
print(ticket_price)
#遍历输出
for key in ticket_price.keys():
    print(key)
    value=ticket_price.get(key)
    for item in value:
        print(item, '\t', value.get(item))
    print()