'''
문제 K: [PYTHON] Decorator | 꾸미기 귀찮은 세종이

세종이는 함수 디버깅(function debugging)을 위하여, 매 함수가 실행될때마다 아래와 같은 표식을 통해 구분하기로 하였다.

============== (14개)
function debug
==============

모든 함수에 출력을 넣다보니 매우 비효율적이고, 디버깅 필요가 없어진 경우에 삭제하기 너무 어려웠다.
그 와중에 수업시간에 배운 Decorator 가 떠올랐고.. 이를 활용해보고 싶어졌다.

세종이를 위해서, 함수 실행전에 위에 같은 function debug 를 출력할 수 있게 해주는 Decorator( func_debug(func) ) 를 작성하시오.

*** Decorator 이름에 주의하시오.
*** 후 입력 코드를 확인하세요.

출력
기본 함수 출력과
Decorator 된 함수 출력

출력 예시
SASA
==============
function debug
==============
Python
'''


def de_func(original_function):
    def wrapper_function():
        print('==============')
        print('function debug')
        print('==============')
        return original_function()

    return wrapper_function

# 선 입력 Rear Code

def print_sasa():
    print("SASA")


@de_func
def print_python():
    print("Python")


print_sasa()
print_python()