'''
문제 G: [PYTHON] Class 를 활용하기 | 계산기

세종시는 수업시간에 봤던, 계산기 Class 를 보고, 덧샘 뿐만 아니라 뺄샘, 곱샘을 할 수 있도록 Code 를 작성하였다.
세종이가 작성한 Calculator Class 를 활용하여,

사용자로부터 3개의 정수를 입력 받아, 첫번째 입력은 덧샘, 두번째 입력은 뺄샘, 세번째 입력은 곱샘을 한 결과를 출력하시오.
(모든 계산은 누적값임)

예를 들어, 사용자가 1, 2, 3 을 입력했다면
1
-1
-3
이 출력되어야 함.

이 진행되는 계산 결과를 출력하시오.

입력
3개의 정수가 Enter 로 구분되어 입력됨

입력되는 정수의 범위
0<a,b,c<100

출력
첫번째 입력은 덧샘을 한 결과
두번째 입력은 뺄샘을 한 누적 결과
세번째 입력은 곱샘을 한 누적 결과

입력 예시
1
2
3

출력 예시
1
-1
-3
'''

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a):
        self.result += a
        return self.result

    def minus(self, a):
        self.result -= a
        return self.result

    def mul(self, a):
        self.result *= a
        return self.result

# 선 입력 Front Code (1~16 Line)

acal = Calculator()

a = input()
b = input()
c = input()

ar = acal.add(int(a))
print(ar)
ar = acal.minus(int(b))
print(ar)
ar = acal.mul(int(c))
print(ar)