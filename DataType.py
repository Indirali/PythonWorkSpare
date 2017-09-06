# 转义命令\转义字符串
print("I’m \"ok\"")
print("I\'m learning\nPython.")
print("\\n")
print("\\\t\\")

# 转义字符r'' 表示''内部的字符串默认不转义,单引号双引号都可以
print(r"\\\t\\")
print(r'\\\n\\')

# 如果字符串有很多换行，用\n写在一行不好阅读， 可以使用"""..."""表示多行内容
print("""
    line1
    line2
    line3
    """)

# Boolean 首字母必须大写（True,False）
print(3 > 2)
print(True)

# Boolean 运算 and,or,not

True and True
True or False
not True
5 > 3 and 3 < 1

age = int(input("输入年龄："))

if age >= 18:
    print("adult")
else:
    print("teenager")

# 空值为None
None

# 变量
a = 1
t_007 = "T007"
Answer = True
a = 123
print(a)
a = "ABC"
print(a)

# 常量 大写表示(可变),只不过通常用大写表示
PI = 3.14

# 除法 /除法计算结果是浮点数
print(9 / 3)
print(10 / 3)

# 除法 //表示计算结果是整数
print(9 // 3)
print(10 // 3)

# 数据格式化
print("Hello, %s" % "world")
print("Hi, %s, you have $%d." % ("Michael", 10000))

# %d 整数  %f 浮点数  %s 字符串类型 %x 十六进制整数
