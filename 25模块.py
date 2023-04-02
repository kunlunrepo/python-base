import calc

print(calc.add(10,30))

from calc import add #只导入一个函数
print(add(10,40))

from mypkg import pkgcalc

print(pkgcalc.add(10,1))