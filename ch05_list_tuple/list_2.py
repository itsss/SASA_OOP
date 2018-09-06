my_list = ['p', 'y', 't', 'h', 'o', 'n']  # list 타입 생성
my_str = "python"  # 문자열 타입

print("\n======= + 연산 =======")
print("리스트 연산 결과: ", end='')
print(my_list + my_list)
print("문자열 연산 결과: ", end='')
print(my_str + my_str)

print("\n======= * 연산 =======")
print("리스트 연산 결과: ", end='')
print(my_list * 4)
print("문자열 연산 결과: ", end='')
print(my_str * 4)

print("\n======= 분할(slicing) 연산 =======")
print("리스트 연산 결과: ", end='')
print(my_list[0:3])
print("문자열 연산 결과: ", end='')
print(my_str[0:3])

print("\n======= 확장 분할 연산 =======")
print("리스트 연산 결과: ", end='')
print(my_list[::3])
print("문자열 연산 결과: ", end='')
print(my_str[::3])

print("\n======= 확장 분할 연산 역순=======")
print("리스트 연산 결과: ", end='')
print(my_list[::-1])
print("문자열 연산 결과: ", end='')
print(my_str[::-1])

print("\n======= 상호 변환 =======")
print("문자열 > 리스트 변환 결과: ", end='')
print(list(my_str))
print("리스트 > 문자열 변환 결과: ", end='')
print(''.join(my_list))