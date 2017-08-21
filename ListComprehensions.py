import os

# 列表生成式即List Comprehensions

list(range(1, 11))

print([x * x for x in range(1, 11)])

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print([x * x for x in range(1, 11) if x % 2 == 0])

# 两层循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

# 列出当前目录下的所有文件和目录名
print([d for d in os.listdir('.')])
