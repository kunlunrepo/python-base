# carrot='红萝卜'
# carrot_count=220
# carrot_price=2.5
#
# potato='新鲜土豆'
# potato_count = 300
# potato_price= 2.6
#
# green_bean='青豆皮'
# green_bean_count=26
# green_bean_price=6.8
#
# print('名称\t数量\t单价\t小计')
# print(f'{carrot}\t{carrot_count}\t{carrot_price}\t{carrot_count*carrot_price}')
#
# import turtle
#
# turtle.pensize(3)
# turtle.circle(20)
# turtle.circle(40)
# turtle.circle(80)
# turtle.circle(160)

for i in range(1,10):
    for j in range(1, i+1):
        print(f'{i}*{j}={i*j}', end='\t')
    print()