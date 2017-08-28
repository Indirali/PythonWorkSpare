from functools import reduce


def f(x):
    return x * x


# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
r = map(f, range(0, 10))
print(list(r))


def add(x, y):
    return x + y


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
reduce(add, [1, 3, 5, 7, 9])
print(reduce(add, [1, 3, 5, 7, 9]))


def fn(x, y):
    return x * 10 + y


print(int(reduce(fn, [1, 3, 5, 7, 9])))
