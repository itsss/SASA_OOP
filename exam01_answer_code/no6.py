'''
하루 물 권장량은 2L로 알려져 있다. 하지만 권고량의 50%도 마시지 않는다는 설문조사 결과를 보고 하루에 물을 얼마나 섭취했는지를 저장하고 안내하는 'DailyWater' Class를 제작하고자 한다.
아래 코드의 실행 결과를 보고 'DailyWater' Class를 작성하시오.
'''

class DailyWater:
    def __init__(self, a):
        self.a = a
        self.b = 0

    def __add__(self, other):
        self.b += other

    def status(self):
        print("%s 가 먹은 물의 양: %s" % (self.a, self.b))

dw1 = DailyWater('kadragon')
dw1 + 100
dw1 + 400
dw1.status()