import datetime


class Student(object):
    def __init__(self, score, age, birth):
        self.__score = score
        self.__age = age
        self.__birth = birth

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100！')
        self.__score = value

    @property
    def age(self):
        return datetime.date.today() - datetime.timedelta(self.__birth)

    @property
    def birth(self):
        return self.__score

    @birth.setter
    def birth(self, value):
        self.__birth = value


s = Student(90, 10, 20170101)
s.score = 60
print(s.score)
