class Calculator(object):
    def __init__(self):
        self.current = 0
    def add(self, amount):
        self.current += amount
    def getCurrent(self):
        return self.current