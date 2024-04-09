import math

class Calculator:
    def __init__(self,value):
        self.value = value

    def add(self,other):
        self.value += other

    def divide(self,other):
        self.value /= other

    def subtract(self, other):
        self.value -= other

    def get_result(self):
        return self.value

class Calculator2(Calculator):
    def __init__(self, value):
        super().__init__(value)

    def sqrt(self):
        self.value = math.sqrt(self.value)

if __name__ == "__main__":
    c = Calculator2(7)
    c.add(9)
    c.divide(2)
    c.subtract(2)
    c.sqrt()
    print(c.get_result())
