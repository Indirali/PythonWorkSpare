from collections import Iterable

# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代.
# list中的值如果是int类型,输出的值要加str()
d = {'a': 1, 'b': 2, 'c': 3}
for key, val in d.items():
    print("key:" + key + "\t" + "value:" + str(val))

for ch in 'ABC':
    print(ch)

# 如何判断一个对象是可迭代对象
print(isinstance("ABCD", Iterable))  # str是否可迭代
print(isinstance([1, 2, 3], Iterable))  # list是否可迭代
print(isinstance(123, Iterable))  # 整数是否可迭代
print(isinstance(str(123), Iterable))  # 整数转为字符串后是否可迭代

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
