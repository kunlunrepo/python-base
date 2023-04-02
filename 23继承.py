

class A:
    def __init__(self,width, height):
        self.width=width
        self.height=height


class B(A): #单继承
    def __init__(self,width, height, weight):
        super().__init__(width,height) # 调用父类的初始化方法
        self.weight=weight

class D:
    def __init__(self,brand):
        self.brand=brand

class C(A,D): #多继承 重写时，A类的方法优先于D类
    def __init__(self,width, height, brand, type):
        A.__init__(self,width,height)
        D.__init__(self,brand)
        self.type = type

    def show(self):
        print('高', self.height)
        print('宽', self.width)
        print('品牌', self.brand)
        print('类型', self.type)

c=C(width='8cm', height='20cm', brand='小米', type='米优优')
c.show()