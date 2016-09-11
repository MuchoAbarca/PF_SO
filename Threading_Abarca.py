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
