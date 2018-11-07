import threading
import time
import random

class client_thread(threading.Thread):
    def __init__(self, clientname, sec):
        threading.Thread.__init__(self)
        self.clientname = clientname
        self.sec = sec

    def run(self):
        while True:
            print("%s - delay %f" % (self.clientname, self.sec))
            time.sleep(self.sec)

client = []
for i in range(10):
    client.append(client_thread("client" + str(1), random.randint(1, 10)))

for i in range(10):
    client[i].start()