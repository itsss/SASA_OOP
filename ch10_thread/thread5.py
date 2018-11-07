# 1초마다 A를 출력하고,
# 1.5초마다 B를 출력하고
# 2초마다 C를 출력하는 프로그램을 만들어 보자.

import threading
import time

def client_thread(clientname, sec):
    for i in range(10):
        print(clientname)
        time.sleep(sec)

clientA = threading.Thread(target=client_thread, args=("A", 1))
clientB = threading.Thread(target=client_thread, args=("B", 1.5))
clientC = threading.Thread(target=client_thread, args=("C", 2.0))

clientA.start()
clientB.start()
clientC.start()