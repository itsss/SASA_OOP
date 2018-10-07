'''
문제 J: [PYTHON] function | 함수에 함수를 매개변수로 던져주기!

세종이는 수업시간에 python 에서 함수는 객체이기 때문에, 함수의 인자로 넣어줄 수 있다는 것을 알게 된 후
함수를 매개변수로 하는 함수를 짜보고자 하였다.

세종이가 만들려는 함수는 다음과 같은 특성을 가지고 있다.
함수1개, 정수로 이루어진 리스트, 정수 1개를 입력 받아
리스트에 담겨있는 정수 1개를 a 라 하고, 나중에 받은 정수 1개를 b 라고 할때
매개변수로 입력 받은 함수 f(a, b)의 결과를 모아 list로 반환한다.

예를 들어,
func(a, b):
    return a+b
정수 리스트: [1, 2, 3, 4, 5]
정수 1개: 5
가 입력된다면, 반환된 list 값은 [6, 7, 8, 9, 10] 이된다.

세종이가 만들고 싶은 함수[ convert_int(func, list, i) ]를 코딩하시오.

입력 예시
1 2 3
3

출력 예시
[1, 8, 27]
'''

def convert_int(func, list, k):
    result = []
    for i in list:
        result.append(func(i, k))
    return result

# 선 입력 Rear Code
list = map(int, input().split())
k = int(input())

convert_list = convert_int(pow, list, k)
print(convert_list)