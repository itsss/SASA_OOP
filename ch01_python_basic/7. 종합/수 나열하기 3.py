a, b, c, d = input().split()
A = int(a)
B = int(b)
C = int(c)
D = int(d)

for i in range(D-1):
    A = A * B + C
print(A)