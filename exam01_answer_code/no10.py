'''
알파벳으로 구성된 문자열을 입력받아, 구성하고 있는 알파벳과 갯수를 분석하기 위해 Dictionary Type을 활용하기로 하고 다음과 같이 Code를 작성하였다.
하지만 실행결과 KeyError가 발생하여 원하는 대로 실행되지 않았다.

에러를 보고 문제를 찾아낸 세종이는 Code를 수정하여 아래와 같은 결과를 얻을 수 있었다.

Python Software Foundation이 제공하는 설명서 중 setdefault(key[, default])와 update(Other)에 대한 내용을 참고하여
세종이가 수정한 Code를 작성하시오.
'''

n_string = "SASA"
count_char = {}

for i in in_string:
    count_char.setdefault(i, 0)
    count_char[i] += 1

print(count_char)