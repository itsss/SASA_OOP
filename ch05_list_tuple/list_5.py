my_list = ['hi', 'python', 3.5]
del my_list[2]
print(my_list)
# 결과: ['hi', 'python']

my_list = [1, 2, 3, 4, 5]
del my_list[0:4]
print(my_list)
# 결과: [5]

my_list = [1, 2, 3, 4, 5]
del my_list[::2] #위치 기반으로 삭제
print(my_list)
# 결과: [2, 4]

my_list = [1, 2, 3, 4, 5]
my_list.remove(3) #값 기반으로 삭제
print(my_list)
# 결과: [1, 2, 4, 5]

my_list = [1, 2, 3, 4, 5]
print(my_list.pop()) #값을 꺼내주고 삭제
# 결과: 5
print(my_list)
# 결과: [1, 2, 3, 4]

print(my_list.pop(0)) #Index 지정도 가능 
# 결과: 1
print(my_list)
# 결과: [2, 3, 4]