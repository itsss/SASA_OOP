a,b,c = input().split()
x = int(a)
y = int(b)
z = int(c)

day = 1
while(day % x != 0 or day % y != 0 or day % z != 0):
    day += 1

print(day)