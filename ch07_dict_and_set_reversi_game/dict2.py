popul_dict = {'China': 1367485388, 'India': 1251695584, 'Indonesia': 321368864, 'America': 513949445, 'Brazil': 255993674}

popul_dict['Korea'] = 51529338

popul_dict.update({'Korea': 51529777, 'Japan': 127103388})
print(popul_dict)
# 결과: {..., 'Brazil': 255993674, 'Korea': 51529777, 'Japan': 127103388}

my_dict = {'c': 3, 'd': 4, 'a': 1, 'b': 2}
print(my_dict.setdefault('a', 100))  # 결과: 1
print(my_dict)  # 결과: {'c': 3, 'd': 4, 'a': 1, 'b': 2}

print(my_dict.setdefault('e', 100))  # 결과: 100
print(my_dict)  # 결과: {'c': 3, 'd': 4, 'a': 1, 'b': 2, 'e': 100}

# 값을 삭제하는 방법..!
del my_dict['c']
print(my_dict)  # 결과: {'d': 4, 'a': 1, 'b': 2, 'e': 100}

# 값이 있는지 확인하는 방법..!
print('d' in my_dict)  # True

# List <> Dictionary

popul_dict = {'China': 1367485388, 'India': 1251695584, 'Indonesia': 321368864, 'America': 513949445, 'Brazil': 255993674}
print(list(popul_dict))
# 결과: ['China', 'India', 'Indonesia', 'America', 'Brazil']

popul_list = [['China', 1367485388], ['India', 1251695584], ['America', 513949445], ['Indonesia', 321368864], ['Brazil', 255993674]]

popul_convert_dict = dict(popul_list)
print(popul_convert_dict)
# 결과: {'China': 1367485388, 'India': 1251695584, ...

test = ['ab', 'cd']
print(dict(test))
# 결과: {'a': 'b', 'c': 'd'}
