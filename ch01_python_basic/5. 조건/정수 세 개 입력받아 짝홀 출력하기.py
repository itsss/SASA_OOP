a = map(int, input().split()) #List형 저장
for i in a:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")