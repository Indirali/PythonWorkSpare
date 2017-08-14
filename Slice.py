
# 切片 取前3个元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])

# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
print(L[:3])
print(L[1:3])

# 同样支持倒数切片
print(L[-2:])
print(L[-2:-1])

L = list(range(100))
print(L)
# 前十个数
L[:10]

# 后十个数
L[-10:]

L[10:20]

# 前10个数，每两个取一个：
L[:10:2]

# 每五个取一个：
L[::5]

'ABCDEFG'[:3]
