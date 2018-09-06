"""
Title       Calculator (Class 구현)
Author      ITSC (Taewon Kang)
Date        2018.08.30
"""

class Calculator:
    def __init__(self): #초기화
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))

print(cal2.adder(3))
print(cal2.adder(7))