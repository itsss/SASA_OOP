a, b, c = input().split()

d = int(a)
e = int(b)
f = int(c)

for i in range(0, d):
    for j in range(0, e):
        for k in range(0, f):
            print(i, j, k)

print(d*e*f)