lst = [
    {'a': 10, 'b': 8, 'c': 100},
    {'a': 13, 'b': 100, 'c': 98},
    {'a': 3, 'b': 87, 'c': 48}
]

# key是排序的规则 x表示的是列表中的元素，列表中的元素是字典类型，字典取值是get()
lst.sort(key= lambda x:x.get('a')) # 升序  lambda表达式的写法

print(lst)