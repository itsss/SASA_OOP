"""
Title       제대로 된 계산기 만들기
Author      ITSC (Taewon Kang)
Date        2018.08.30
"""

class Cal:
    def set_data(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

a = Cal()
#print(a.first) -- set_data가 실행되지 않았으므로, 에러가 남
b = Cal()

a.set_data(1, 3)
b.set_data(10, 4)

print(a.sum())
print(b.div())