'''
문제 B: [PYTHON] .replace() 사용 해보기

사용자로부터 문자열을 입력 받아, 띄어쓰기를 제거하시오.

입력
사용자로부터 문자열을 입력 받음

출력
띄어쓰기를 제거하여 출력

입력 예시
Sejong Academy of Science and Arts

출력 예시
SejongAcademyofScienceandArts
'''

s = input()
s = s.replace(' ', '')
print(s)