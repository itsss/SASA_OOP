'''
문제 I: [PYTHON] Exception | 사람들은...ㅠ

세종이는 정수 두개 a, b 를 입력 받아,
a로 b를 나눠 출력하는 Method 를 만들어서 사람들에게 배포하였다.

입력 값으로 1 < a, b < 100로 안내하였지만,
사람들은 0으로 나누는것을 시도해 ZeroDivisionError 발생시킨다던지, a b와 같은 형태로 입력하지 않아 ValueError 를 발생시켰다. (나쁜 사람들..)

자, 세종이를 대신하여 정수 두개 a, b를 Enter 로 구분되어 입력 받아,
a/b 를 출력하면서,
위에 2개의 에러 중 1개를 제어할 수 있는 프로그램을 만들어보자.

ZeroDivisionError 가 발생할 경우, 프로그램이 종료되지 않고 [ B must not be zero. ] 를 출력하고,
에러가 발생하지 않을 경우 정상적으로 값이 출력 프로그램을 작성하시오.

반드시, try ~ except ~ else 를 사용하시오.
if b == 0: 와 같은 구분은 인정하지 않습니다.
'''

try:
   a = input()
   b = input()
   print(int(a)/int(b))
except ZeroDivisionError:
   print('[ B must not be zero. ]')