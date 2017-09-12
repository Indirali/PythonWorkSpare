# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
class Student(object):
    pass


bart = Student()

print(bart)

bart.name = "Bart Simpson"
print(bart.name)


# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student("lindira", 90)
bart.print_score()


# 为了保证内部属性不被外部访问，可以把属性的名称前加上两个下划线__
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


bart = Student("Admin", 60)
print(bart.get_name())
print(bart.get_score())
bart.set_name("lindira")
bart.set_score(100)
print(bart.get_name())
print(bart.get_score())


# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass）
# 被继承的class称为基类、父类或超类（Base class、Super class）
class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
dog.run()

cat = Cat()
cat.run()


class Student(object):
    pass


s = Student()
s.name = 'Michael'
print(s.name)


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


class Student(object):
    __slots__ = ('name', 'age')


s = Student()
s.name = 'Michael'
s.age = 25


# s.score = 99


class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 9999
print(g.score)
