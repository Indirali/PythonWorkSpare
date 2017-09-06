d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value。
d['Admin'] = 65

# 若key相同会覆盖值
d['Admin'] = 75
print(d)

# key不存在的错误，有两种办法，一是通过in判断key是否存在：
'Thomas' in d
print('Thomas' in d)

# 通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
d.get('Thomas')
d.get('Thomas', -1)
print(d)

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Admin')
print(d)

# dict内部存放的顺序和key放入的顺序是没有关系的。

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 2, 3])
print(s)

# 重复元素在set中自动被过滤
s = set([1, 1, 2, 2, 3, 3])
print(s)

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)
print(s)

# 通过remove(key)方法可以删除元素：
s.remove(4)
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# set是不变对象，而list是可变对象。

a = ['c', 'b', 'a']
a.sort()  # 变完后不保存
print(a)

a = 'abc'
print(a.replace('a', 'A'))  # 变完后不保存
print(a)
