'''
다음은 Python Software Foundation이 제공하는 설명서 중 'copy'에 대한 내용이다.
이 내용을 참고하여, 다음 Code의 실행 결과가 나오도록 copy를 활용하여 Code를 완성하시오.
'''

import copy

b = [1,4,7,9,[2,3,4,5]]

c = copy.copy(b)
d = copy.deepcopy(b)

b[4][0] = 100

print(c[0])
print(c[4][0])

print(d[1])
print(d[4][0])