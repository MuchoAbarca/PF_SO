import random
import threading

def list_append(count, id, out_list):
    for i in range(count):
        out_list.append(random.random())

if __name__=="__main__":
    size=100
    threads=5
    jobs=[]

    for i in range(0, threads):
        out_list=list()
        thread=threading.Thread(target=list_append(size, i, out_list))
        jobs.append(thread)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print "lista completada"