try:
   f = open('test.txt', 'x')
except FileExistsError:
   print('FileExistsError')
else:
   f.write('+_____+')
   f.close()
