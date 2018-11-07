import threading

Q = 1000000
lock = threading.Lock()

def drink(max):
   global Q
   for i in range(max):
       lock.acquire()
       Q -= 1
       lock.release()

A = threading.Thread(target = drink, args = (500000, ))
B = threading.Thread(target = drink, args = (500000, ))

A.start()
B.start()

A.join()
B.join()

print(Q)