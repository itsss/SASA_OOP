# C 언어와 달리, 조건문을 사용할 때 { } 를 사용하지 않고, : 로 구분한다.
a = 3
if a > 1:
    print("a is greater than 1")
elif a == 0:
    print("a is 0")
else:
    print("a is not greater than 1")

print('='*50)

# [ ] 은 python 자료형 중 리스트로, C 언어의 배열과 비슷하다.
# 아래 for 문의 의미는, [1, 2, 3] 리스트에서 index가 0 작은 것부터 꺼내,
# a에 넣어 반복하라는 의미이다.
for a in [1, 2, 3]:
    print(a)

print('='*50)

i = 0
while i < 3:
    i = i + 1  # i += 1
    print(i)