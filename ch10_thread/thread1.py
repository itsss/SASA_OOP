import threading  # Thread를 사용하기 위해서 가져오기
import time       # time.sleep() 사용


def client_thread(clientname, sec):
    for i in range(3):
        print("%s - 지연 %d" % (clientname, sec))
        time.sleep(sec)


# threading.Thread를 활용 | target은 사용하고자 하는 method명 | args는 전달하고자 하는 매개변수)
clientA = threading.Thread(target = client_thread, args = ("clientA", 0.1))
clientB = threading.Thread(target = client_thread, args = ("clientB", 0.2))

# 만들어둔 Thread 실행
clientA.start()
clientB.start()