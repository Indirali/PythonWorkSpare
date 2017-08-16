# 调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。
abs(-20)  # 输出绝对值

# max函数可以接收多个参数，返回最大的那个
print(max(1, 2, 3, 4, 5, 6, 7, 8, 9))

# 把其他类型转为特定类型
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(bool(1))
print(bool(''))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs  # 变量a指向abs函数
a(-1)  # 所以也可以通过a调用abs函数


# 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


def power(x):
    return x * x

print(power(5))


def powers(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(powers(5, 3))


# 设置方法默认值
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('LiFan', 'F')

# 只有与默认参数不符的学生才需要提供额外的信息：
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')

# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# def add_end(L=[]):  # 错误的
#     L.append('END')
#     return L


def add_end(l=None):
    if l is None:
        l = []
    l.append('END')
    return l

print(add_end([1, 2, 34, 5, 6]))

# 可变参数就是传入的参数个数是可变的


def calc(*numbers):
    sums = 0
    for n in numbers:
        sums = sums + n * n
    return sums

print(calc(1, 2))
print(calc())


# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数
person('Michael', 30)

# 也可以传入任意个数的关键字参数
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
