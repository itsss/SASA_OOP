'''

다음 Code를 보고, 실행 결과를 작성하시오.

'''

my_list = [1,2,3,4,5]

print(my_list[-1]) # 5
print(my_list.pop()) # 5
print(my_list.pop(1)) # 2

my_list = [1,2,3,4,5]
my_list.remove(3)
print(my_list) # [1, 2, 4, 5]

my_list = [1,2,3,4,5]
my_list.append([4, 5])
print(my_list) # [1, 2, 3, 4, 5, [4, 5]]

my_list = [1,2,3,4,5]
print(my_list[::-1]) # [5, 4, 3, 2, 1]

sasa = "Sejong Academy of Science and Arts"
print(sasa[2:6:2]) # jn

a=10
b=10
print(id(a) == id(b)) # True