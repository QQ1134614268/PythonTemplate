class Student(object):

    def __init__(self):
        self._score = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('分数必须是整数才行呐')
        if value < 0 or value > 100:
            raise ValueError('分数必须0-100之间')
        self._score = value

