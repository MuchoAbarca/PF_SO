import os
from time import sleep
from os import system
from multiprocessing import Process

root = '/home'
pattern = []

def start():
    print ('Hola, soy tu task manager. Que te gustaria hacer?\n \
     \nA) Obtener Una Lista De Tus Procesos                     \
     \nB) Crear Un Proceso                                      \
     \nC) Matar Un Proceso                                      \
     \nD) Guardar Tus Procesos                                  \
     \nE) Hacer Map Disk\n')

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
        print ('M o s t r a n d o  D i s c o')
        sleep(0.5)
        Datos_MapDisk()
        start()
        
def child():
    print('Hello from child', os.getpid())
    os._exit(0)


def process_maker(num_process):
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

def get_file(pattern):
    total_B=0
    total_num=0

    for path, subdirs, files in os.walk(root):
        for name in files:
            for a in pattern:
                if fnmatch(name, a):
                    total_B+=(get_size(os.path.join(path, name)))
                    total_num+=1
    print total_num
    print bytes2human(total_B)

def Datos_MapDisk():
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

def Guardando():
    os.system("ps aux > process_list.txt")
    print ("Se lista de procesos se ha generado")

start()
