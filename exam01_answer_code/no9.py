'''
다음은 Python Software Foundation이 제공하는 설명서 중, math.factorial(x)에 관한 설명이다.
다음 설명을 읽고, 아래 Code의 실행 결과를 작성하시오.
'''

import math

def try_factorial(in_int):
    try:
        print(math.factorial(in_int))

    except ValueError:
        print('invaild value')
        
try_factorial(5)
try_factorial(0)
try_factorial(0.4)