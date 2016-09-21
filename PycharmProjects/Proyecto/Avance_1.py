import os
import time
from multiprocessing import Process

def start():
    print ('Hola, soy tu task manager.                  \
    Que gustarias hacer? \n                             \
    \nA) Obtener Una Lista De Tus Procesos              \
    \nB) Guardar Tus Procesos \nC) Hacer Map Disk\n')   
    Accion = raw_input()
    if(str(Accion).upper() == 'A'):
        Lista_Procesos()
        start()
    if(str(Accion).upper() == 'B'):
        print ('\nG u a r d a n d o  P r o c e s o')
        sleep(0.5)
        Guardando()
        start()
    if(str(Accion).upper() == 'C'):
        print ('Mostrando Disk')
        Datos_MapDisk()
        start()
def child():
    print('Hello from child', os.getpid())
    os._exit(0)


def parent(num_process):
    for num in range(1, num_process):

        newpid = os.fork()
        if newpid == 0:
            child()

def process_killer(process_id):
    os.kill(process_id, 0)
    #revisar si en efecto se acabó con el proceso
    try:
        os.kill(proccess_id, 0)
    except OSError:
        return False
    else:
        return True
    
def Lista_Procesos():
    print('Gusta ordenarlo por...\n \tA) CPU\n \tB) Memoria')
    X = raw_input()
    if(str(X).upper() == 'A'):
        os.system('ps -e -o pcpu,cpu,cputime,args --sort pcpu ')
    if (str(X).upper() == 'B'):
        os.system('ps aux --width 30 --sort -rss')
        
def get_size(the_path):
    path_size = 0
    for path, directories, files in os.walk(the_path):
        for filename in files:
            path_size += os.lstat(os.path.join(path, filename)).st_size
        for directory in directories:
            path_size += os.lstat(os.path.join(path, directory)).st_size
    path_size += os.path.getsize(the_path)
    return path_size

def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i+1)*10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

def Datos_MapDisk():
    rootDir = '/home'
    content_list = []
    for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
        content_list.append(dirName)

    size_list = []
    for i in content_list:
        size_list.append(bytes2human(get_size(i)))
        print(i, bytes2human(get_size(i)))

def Guardando():
    os.system("ps aux > process_list.txt")
    print ("Se lista de procesos se ha generado")

start()
