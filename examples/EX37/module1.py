class Something:
    def __init__(self,value1, value2):
        self.value1 = value1
        self.value2 = value2
    def addValues(self):
        self.total = self.value1 + self.value2
        print self.total
newValue = Something(5, 9)

newValue.addValues()