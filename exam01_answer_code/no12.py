'''

세종이는 Online Judge에서 201부터 210까지의 합을 구하는 문제를 두 가지 방법으로 풀다가,
range를 활용한 Code가 더 메모리를 적게 사용한다는 것을 알게 되었다.

다음은 'class range'에 관한 Python Software Foundation이 제공하는 설명서 중 일부다.
설명서를 참고하여 아래 Code의 실행 결과를 작성하시오.

'''

print(list(range(5)))

print(list(range(1,5)))

print(list(range(0,20,5)))

print(list(range(0,10,4)))

print(list(range(0,-5,-2)))

print(list(range(0)))

print(list(range(1, 0)))