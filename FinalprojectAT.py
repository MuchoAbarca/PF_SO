import os

#Esta es la solucion que presente en mi tarea, creo que debo de tener la que se presento en la clase
#Si la encuentro la agrego el domingo
def child():

    print('Hello from child', os.getpid())
    os._exit(0)


def parent():
    for num in range(1, 11):

        newpid = os.fork()
        if newpid == 0:
            child()


parent()