'''
문제 H: [PYTHON] Class 상속? | 귀찮은 세종이

덧샘과 뺄샘, 그리고 곱샘을 할 수 있는 계산기를 만든 세종이는.. 교사 강동욱으로부터 '나눗샘도 할 수 있는 계산기를 만들어 보렴~' 이라는 이야기를 듣고..
"나중에 만들어야지" 라고 생각한 후 __init__ 만 만들고 남겨두었다.

미 완성되어 있는 클래스를 상속하여, 두 정수 (a,b)를 입력 받아,
a/b 값을 돌려주는 'CompleteCal Class'와 'div' 메소드를 완성하시오.

입력
1 < a, b < 101 (신경 쓸 필요 없음)

출력
a/b 결과

입력 예시
6 3

출력 예시
2.0
'''

class UnCompleteCal:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def div(self):
        pass

# 선 입력 Front Code
# ================
class CompleteCal(UnCompleteCal):
    def div(self):
        return int(a) / int(b)
# ================
# 선 입력 Rear Code

a, b = input().split()
div_cal = CompleteCal(int(a), int(b))
print(div_cal.div())