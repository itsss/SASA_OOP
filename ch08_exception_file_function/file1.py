f = open('test.txt', 'w')
f.write('Python')
f.close()

f = open('test.txt', 'r')
string = f.read()
print(string)  # 출력 값: Python
f.close()

f = open('test.txt', 'a')
return_value = f.write(' is simple')
print(return_value)  # 출력 값: 10
f.close()
