
#类
class Phone:

    #方法 是Phone“父类”中的方法 一个类默认继承object类
    def __init__(self, brand, goods_name,goods_id,address,color):  #方法中的第一个参数必须是self
        # 实例属性
        self.brand = brand
        self.goods_name = goods_name
        self.goods_id = goods_id
        self.address = address
        self.color = color

    #实例方法
    def call(self,name):
        print(f'正在使用{self.brand}品牌的手机，给{name}打电话')

    def info(self):
        print(f'品牌:{self.brand}')
        print(f'商品名称:{self.goods_name}')
        print(f'商品id:{self.goods_id}')
        print(f'产地:{self.address}')
        print(f'机身颜色:{self.color}')


"""
  __new__方法用来创建对象初始化内存
  __init__方法用来赋值
"""

p1=Phone('荣耀',"荣耀6", '2023040201', '中国', '银色系')

p2=Phone('vivo',"vivo7", '2023040202', '中国', '黑色系')

p3=Phone('苹果',"苹果14", '2023040203', '中国', '紫色系')

print("*"*20)
p1.info();

print("*"*20)
p2.info();

print("*"*20)
p3.xp=4800 #动态绑定实例属性
p3.info();
print(f"后置摄像头{p3.xp}万像素")

print("-"*20)
p3.call("韩梅梅")

print("*"*20)
p1.brand = "华为"
p1.info()



class Student:
    #类属性
    school = 'msb'
    def __init__(self,stu_no, stu_name, stu_gender):
        self.stu_no = stu_no
        self.stu_name = stu_name
        self.stu_gender = stu_gender

    def info(self):
        print(f'name:{self.stu_name}')
        print(f'stuno:{self.stu_no}')
        print(f'gender:{self.stu_gender}')

    @classmethod # 装饰器
    def cmthod(cls):
        print('我是类方法') # 不能使用实例属性或实例方法

    @staticmethod
    def smethod():
        print('我是静态方法')


print("*"*20)
stu=Student(1001, '张一曼', '女')
stu.info()

Student.cmthod()
Student.smethod()