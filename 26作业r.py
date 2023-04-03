import random


def strong(count):
    ball=''
    for i in range(count):
        white=random.sample(range(1,60), 5) #从序列seq中选择n个随机独立的元素
        for item in white:
            ball+=str(item).zfill(2)+' ' # 补零之后的字符串的长度为2
        red=random.choice(range(1, 36))
        ball+=' '+str(red).zfill(2)+'\n'
    return ball

count=eval(input('请输入彩票注数：\n'))

file=open('a.txt', 'w', encoding='utf-8')
file.write(strong(count))
file.close()