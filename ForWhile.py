names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

s = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    s = s + x

print(s)

# range(5)生成的序列是从0开始小于5的整数
print(list(range(5)))

s = 0
for x in range(101):
    s = s + x
print(s)

s = 0
n = 99
while n > 0:
    s = s + n
    n = n - 2
print(s)
