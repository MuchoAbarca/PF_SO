import threading
import time

class MyThread(threading.Thread):
    def run(q):                                         #Lo que hace run es que recurre al objeto invocable
                                                        # que se pasa al constructor y se declara como el
                                                        # argumento de destino

        print("{} started!".format(q.getName()))        # Se "inicia" el thread
        time.sleep(0.5)
        print("{} finished!".format(q.getName()))       # Se "termina" el thread

if __name__ == '__main__':
    for x in range(5):                                     # Se hace 5 veces
        mythread = MyThread(name = "Thread-{}".format(x + 1))  #Se instancia y se le asigna su identificacion
        mythread.start()                                   # Ahora si se inicia
        time.sleep(0.5)                                     # Esperamos medio segundo para generar otro

#import time
#import thread
#def print_time( threadName,delay):
#    count = 0
#    while count < 5:
#        time.sleep(delay)
#        count += 1
#        print "%s: %s" % (threadName,time.ctime(time.time()))
#try:
#    thread.start_new_thread(print_time,("Thread-1",2, ) )
#    thread.start_new_thread(print_time,("Thread-2",2, ) )
#    thread.start_new_thread(print_time, ("Thread-3", 2,))
#    thread.start_new_thread(print_time, ("Thread-4", 2,))
#    thread.start_new_thread(print_time, ("Thread-5", 2,))
#except:
#    print "I am Bagu"
#while 1:
#    pass

