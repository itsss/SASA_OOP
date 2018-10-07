'''
문제 D: [PYTHON] Dictionary Type

학생들의 키를 입력받아 Dictionary Type 으로 저장하고 이를 활용해보고자 한다.

임의의 학생 10명의 이름과 키가 띄어쓰기로 구분되어 입력될때,
이를 tall['이름'] 과 같은 Dictionary 로 저장하시오.

입력
임의의 학생 10명의 이름과 키가 띄어쓰기로 구분되어 입력

출력
미리 선정된 3명의 키

입력 예시
A 175
B 170
C 183
D 167
E 179
F 182
G 162
H 167
I 179
J 153

출력 예시
153
182
179
'''

tall ={}
for i in range(10):
    a, b = input().split()
    tall[str(a)] = b

# 선 입력 Rear Code
print(tall['J'])
print(tall['F'])
print(tall['E'])