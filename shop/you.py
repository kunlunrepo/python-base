
filename='you.txt' #仓库
cart='cart.txt' #购物车

import os.path

#读数据
def read():
    with open(filename, 'r', encoding='gbk') as file:
        data=file.read()
    return data

#写数据
def write(data_dict):
    with open(filename, 'w', encoding='gbk') as file:
        file.write(str(data_dict))

#显示商品
def display():
    data_dict=eval(read()) # eval函数将字符串转成字典
    # print('商品列表开始', '+'*100)
    for key in data_dict.keys():
        print('_'*100)
        print(key)
        good=data_dict.get(key)
        print(f'商品名称：{good[0]}')
        print(f'商品价格：{good[1]}')
        print(f'库存：{good[2]}')
    # print('商品列表结束', '+' * 100)

#根据编号查询商品
def find_by_id(id):
    data_dict=eval(read())
    if id in data_dict:
        good=data_dict.get(id)
        return True, good
    return False

#读取购物车中的商品
def read_cart():
    with open(cart, 'r', encoding='gbk') as file:
        cart_data=file.read()
    return cart_data

#写入购物车
def write_cart(cart_data_dict):
    cart_data={}
    keys = list(cart_data_dict.keys())
    if os.path.exists(cart):
        cart_data=eval(read_cart())
        with open(cart, 'w', encoding='gbk') as file:
            if keys[0] in cart_data:
                # 修改数量
                cart_data.get(keys[0])[1]+=1
                cart_data.get(keys[0])[3] = cart_data.get(keys[0])[1] * cart_data.get(keys[0])[2] #计算总价
            else:
                # 添加新商品
                cart_data[keys[0]]=cart_data_dict.get(keys[0])
            file.write(str(cart_data))
    else:
        cart_data[keys[0]] = cart_data_dict.get(keys[0])
        with open(cart, 'w', encoding='gbk') as file:
            file.write(str(cart_data))
    print('添加成功')

#显示购物车
def display_cart():
    if not os.path.exists(cart):
        return False
    data_dict=eval(read_cart())
    print('=' * 50, '购物车开始', '=' * 50)
    for key in data_dict.keys():
        print('_' * 100)
        print(f'商品编号：{key}')
        good = data_dict.get(key)
        print(f'商品名称：{good[0]}')
        print(f'购买数量：{good[1]}')
        print(f'单价：{good[2]}')
        print(f'总价：{good[3]}')
    print('=' * 50, '购物车结束', '=' * 50)

#主函数
def main():
    print('+'*50,'进入商场','+'*50)
    print('='*50, '商品展示开始','='*50)
    display()
    print('='*50, '商品展示结束','='*50)
    while True:
        answer=input('选择编号添加进购物车')
        # print('_'*100)
        if not answer.isdigit(): #判断输入是否是数字
            print('再逛逛')
            break
        good_id=eval(answer)
        is_find=find_by_id(good_id)
        if type(is_find)==bool:
            print('要添加的商品不存在')
        else:
            good=is_find[1] #获取商品对象
            # {编号:[名称,数量1,单价，小计]}
            good_dict={good_id:[good[0],1,good[1],1*good[1]]}
            write_cart(good_dict)
            print('_'*100)
            display_cart() #显示购物车
        # print('_'*100)


if __name__ == '__main__':
    main()