import os
import logging
from os import system
from time import sleep
from logging import handler
from fnmatch import fnmatch
from multiprocessing import Process

root = '/home'
pattern = []

def start():
    
    print ('Hola, soy tu task manager. Que te gustaria hacer?\n \
     \nA) Obtener Una Lista De Tus Procesos                     \
     \nB) Crear Un Proceso                                      \
     \nC) Matar Un Proceso                                      \
     \nD) Guardar Tus Procesos                                  \
     \nE) Hacer Map Disk                                        \
     \nS) Salir\n')

    Accion = raw_input()
    if(str(Accion).upper() == 'A'):
        Lista_Procesos()
        start()
    if(str(Accion).upper() == 'B'):
        print ('C r e a n d o  P r o c e s o')
        sleep(0.5)
        process_maker()
        start()
    if (str(Accion).upper() == 'C'):
        print ('M a t a n d o  P r o c e s o')
        sleep(0.5)
        process_killer()
        start()
    if(str(Accion).upper() == 'D'):
        print ('\nG u a r d a n d o  P r o c e s o')
        sleep(0.5)
        Guardando()
        start()
    if(str(Accion).upper() == 'E'):
        Datos_MapDisk()
        start()
    if (str(Accion).upper() == 'S'):
        print ('\nC e r r a n d o')
        sleep(0.3)
        quit()
        
def child():
    
    print('Hello from child', os.getpid())
    os._exit(0)


def process_maker():
    
    for num in range(1, 5):
        newpid = os.fork()
        if newpid == 0:
            child()

def process_killer():
    
    print('Escriba PID')
    process_id = input()
    os.kill(process_id, 0)
    print ('Matamos el proceso: ' + str(process_id))
    
def Datos_MapDisk():
    
     print('Gusta ordenarlo por...\n \tA) Tipo de Archivo\n \tB) Carpetas')
    X = raw_input()
    if(str(X).upper() == 'A'):
        print ('M o s t r a n d o  D i s c o')
        sleep(0.5)
        Datos_MapDisk_Archivo()
    if (str(X).upper() == 'B'):
        print ('M o s t r a n d o  D i s c o')
        sleep(0.5)
        Datos_MapDisk_Carpeta()

        
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

def get_file(pattern):
    
    total_b=0
    total_num=0

    for path, subdirs, files in os.walk(root):
        for name in files:
            for a in pattern:
                if fnmatch(name, a):
                    total_b+=(get_size(os.path.join(path, name)))
                    total_num+=1
    print total_num
    print bytes2human(total_b)

def Datos_MapDisk_Archivo():
    #texto
    print "Archivos de texto:"
    pattern=["*.dic","*.doc","*.diz","*.dochtml","*.exc","*.idx","*.log","*.pdf","*.rtf","*.scp","*.txt","*.wri","*.wtx"]
    get_file(pattern)
    #comprimidos
    print "Archivos comprimidos:"
    pattern = ["*.ace","*.arj","*.bz","*.bz2","*.cab","*.gz","*.ha","*.iso","*.lha","*.lzh","*.r00","*.r01","*.r02","*.r03","*.r0","*.rar","*.tar","*.tbz","*.tbz2","*.tgz","*.uu","*.uue","*.xxe","*.zip","*.zoo"]
    get_file(pattern)
    #video
    print "Archivos de video:"
    pattern=["*.asf","*.avi","*.bik","*.div","*.divx","*.dvd","*.ivf","*.m1v","*.mov","*.movie","*.mp2v","*.mp4","*.mpa","*.mpe","*.mpeg","*.mpg","*.mpv2","*.qt","*.qtl","*.rpm","*.smk","*.wm","*.wmv","*.wob"]
    get_file(pattern)
    #audio
    print "Archivos de audio:"
    pattern=["*.669","*.aif","*.aifc","*.aiff","*.amf","*.asf","*.au","*.audiocd","*.cda","*.cdda","*.far","*.it","*.itz","*.lwv","*.mid","*.midi","*.mp1","*.mp2","*.mp3","*.mtm","*.ogg","*.ogm","*.okt","*.ra","*.rmi","*.snd","*.stm","*.stz","*.ult","*.voc","*.wav","*.wax","*.wm","*.wma","*.wmv","*.xm","*.xmz"]
    get_file(pattern)
    #imagenes
    print "Archivos de imagenes:"
    pattern=["*.ais","*.bmp","*.bw","*.cdr","*.cdt","*.cgm","*.cmx","*.cpt","*.dcx","*.dib","*.emf","*.gbr","*.gif","*.gih","*.ico","*.iff","*.ilbm","*.jfif","*.jif","*.jpe","*.jpeg","*.jpg","*.kdc","*.lbm","*.mac","*.pat","*.pcd","*.pct","*.pcx","*.pic","*.pict","*.png","*.pntg","*.pix","*.psd","*.psp","*.qti","*.qtif","*.rgb","*.rgba","*.rif","*.rle","*.sgi","*.tga","*.tif","*.tiff","*.wmf","*.xcf"]
    get_file(pattern)

def Datos_MapDisk_Carpeta():
    
    rootDir = '/home'
    content_list = []
    for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
        content_list.append(dirName)
    size_list = []
    for i in content_list:
        size_list.append(bytes2human(get_size(i)))
        print(i, bytes2human(get_size(i)))
    
def Guardando():
    
    os.system("ps aux > Process_Log.log")
    print ("Se lista de procesos se ha guardado")
    log_handler = logging.handlers.RotatingFileHandler('Process_Log.log', maxBytes=200000000, backupCount=51)
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(log_handler)
    log.info(os.system("ps aux > Process_Log.log"))

start()
