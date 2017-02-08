class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def sorce(self,sorce):
        if not isinstance(sorce,int):
            raise ValueError('sorce should be integer')
        if sorce < 0 or sorce > 100:
            raise ValueError('sorce should between 0~100')
        self._score = sorce

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,birth):
        self._birth = birth

    @property
    def age(self):
        return 2017 - self._birth
