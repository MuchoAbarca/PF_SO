import threading
import time

class Principal(threading.thread):
    def iniciar(q):

        print ("{} empieza".format(q.getName()))
        time.sleep(1)
        print ("{} termino".format(q.getName()))

for x in range(5):
    elthread =  Principal(name = "Thread-{}".format(x+1))
    Principal.start()
    time.sleep(1)

