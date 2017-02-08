class fib(object):

    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        self.a = 1
        self.b = 1
        for x in range(n):
            self.a, self.b = self.b, self.a + self.b
        return self.a
