a, b, c = input().split()
# 시작 값(a), 등차의 값(d), 몇 번째 인지를 나타내는 정수(n)이 공백을 두고 입력된다.

d = int(a)
e = int(b)
f = int(c)

for i in range(f-1):
    d = d + e

print(d)