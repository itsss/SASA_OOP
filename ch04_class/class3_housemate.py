"""
Title       housemate
Author      ITSC (Taewon Kang)
Date        2018.08.30
"""


class house_sasa:
    sub_title = "SASA "

    def __init__(self, name):  # 객체를 제작할 때 실행됨
        self.target_name = self.sub_title + name

    def go_place(self, place):
        print("%s, %s 로 이동중!" % (self.target_name, place))


class house_sjgl(house_sasa):
    sub_title = "SJGL "

    def go_place(self, place, times):
        print("%s, %s에 %d분 후에 도착 예정..!" % (self.target_name, place, times))

    def __add__(self, other):
        print("%s, %s와 상담중..!" % (self.target_name, other))


pey = house_sjgl("Taewon Kang")

print(pey.target_name)
pey.go_place("S402", 5)
pey + "교장 선생님"
