import math
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction



def multiplication(a, b):
    a = int(a)
    b = int(b)
    return a * b

def division(a, b):
    a = float(a)
    b = float(b)
    return round(b / a, 9)

def squared(a):
    a = int(a)
    return a * a

def squarerooted(a):
    a = float(a)
    return round(math.sqrt(a), 7)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = squared(a)
        return self.result

    def squareroot(self, a):
        self.result = squarerooted(a)
        return self.result