"""
Title       Class 만들기
Author      ITSC (Taewon Kang)
Date        2018.08.30
"""
import random

class Service:
    secret = "시청각실의 장비가 있는 곳으로 가면, 맥실로 갈 수 있는 문이 있지만.. 잠겨있다."
    def set_name(self, name):  # (2)
        self.name = name  # name: (3), self.name(4)
        # set_name 함수가 실행되지 않으면, self.name이 없다고 출력

    def random_select(self, a, b):
        print("%s님, %d와 %d 사이에 선택된 숫자는 %d입니다." % (self.name, a, b, random.randrange(a, b)))

pey = Service() #pey가 일함.
print(pey.secret)
pey.set_name("User") #(1)
pey.random_select(1, 10)