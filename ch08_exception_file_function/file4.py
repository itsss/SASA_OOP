f = open('string.txt', 'r')
for line in f:
   print(line, end='')
f.close()

f = open('string.txt', 'r')
for line in f:
   print(line.strip())
f.close()

with open('string.txt') as f:
   print(f.readlines())
