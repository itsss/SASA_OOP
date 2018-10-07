'''
문제 E: [PYTHON] set Data Type 을 활용해서 중복 제거해보기

사용자로 부터 N개의 정수를 입력 받아 리스트에 저장한다.
그 이후, 중복 값을 제거하고, 오름차순으로 정렬하여 출력하시오.

입력
첫줄에는 입력 받은 데이터의 갯수 1<N<1000
두번째 줄 부터에는 N개의 정수(1<I<500)를 입력 받음.

출력
띄어쓰기로 구분하여 정렬되고 중복이 제거된 정수 목록

입력 예시
10
5
2
1
3
4
3
3
3
1
4

출력 예시
1 2 3 4 5
'''

n = input()
a = []
for i in range(int(n)):
    c = int(input())
    a.append(c)

set_a = list(set(a))
set_a.sort()

for i in set_a:
    print(i, end=' ')