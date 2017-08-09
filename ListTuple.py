
# list是一个有序集合，可以随时添加和删除其中的元素
classmates = ["Michael", "Bob", "Tracy"]
print(len(classmates))
print(classmates[0], classmates[1], classmates[2])

# 获取最后元素 -1,-2....-n
print(classmates[-1])
print(classmates[-2])

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append("Adam")
print(classmates[-1])

# 把元素插入到指定位置
classmates.insert(1, "Jack")
i = 0
for classmate in classmates:
    print(str(i) + " " + classmate)
    i = i + 1

# 删除list末尾元素
classmates.pop()
i = 0
for classmate in classmates:
    print(str(i) + " " + classmate)
    i = i + 1

# 替换某元素的值
classmates[1] = "Admin"
i = 0
for classmate in classmates:
    print(str(i) + " " + classmate)
    i = i + 1

# list 可以存储不同类型的元素
LS = ["Panda", 123, "15gdy"]
i = 0
for L in LS:
    print(str(i) + " " + str(L))
    i = i + 1

# 一个list中的元素也可以是另一个list
LS = ["A", "B", "C", ["D", "E", "F"], "G"]
for L in LS:
    print(L)

print(classmates)

# tuple有序列表元组，tuple一旦初始化就不能修改
Tuple = ("A", "B", "C", "D")
print(Tuple)

# Tuple这个tuple不能变了，它也没有append()，insert()这样的方法。
# 其他获取元素的方法和list是一样的，你可以正常地使Tuple[0]，Tuple[-1]，但不能赋值成另外的元素。

# "可变tuple"
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = "X"
t[2][1] = "Y"
print(t)







