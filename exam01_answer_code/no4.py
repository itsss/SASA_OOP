'''
매개변수가 2개, 또는 3개인 함수 progression(a, b[, c]) 가 있다.
매개변수를 2개만 받을 때에는 a부터 b까지 1씩 증가시키며 띄어쓰기로 구분해 출력하고,
인자가 3개일 때에는 a부터 b까지 c씩 증가시키면서 출력한다. progression(a, b[, c])의 실행 결과를 참고하여,
progression 함수를 완성하시오.
'''

def progression(a, b, step=1):
    x = a
    while x <= b:
        print(x, end=' ')
        x += step

progression(1, 4) # 1 2 3 4
print()
progression(1, 4, 2) # 1 3