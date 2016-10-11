import os
import logging
import plotly.plotly as py
from os import system
from time import sleep
from plotly.graph_objs import *
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

ddef get_file():
    total_bT = 0
    total_numT = 0
    patternT = ["*.dic", "*.doc", "*.diz", "*.dochtml", "*.exc", "*.idx", "*.log", "*.pdf", "*.rtf", "*.scp", "*.txt",
               "*.wri", "*.wtx"]
    total_bC = 0
    total_numC = 0
    patternC = ["*.ace", "*.arj", "*.bz", "*.bz2", "*.cab", "*.gz", "*.ha", "*.iso", "*.lha", "*.lzh", "*.r00", "*.r01",
               "*.r02", "*.r03", "*.r0", "*.rar", "*.tar", "*.tbz", "*.tbz2", "*.tgz", "*.uu", "*.uue", "*.xxe",
               "*.zip", "*.zoo"]
    total_bV = 0
    total_numV = 0
    patternV = ["*.asf", "*.avi", "*.bik", "*.div", "*.divx", "*.dvd", "*.ivf", "*.m1v", "*.mov", "*.movie", "*.mp2v",
               "*.mp4", "*.mpa", "*.mpe", "*.mpeg", "*.mpg", "*.mpv2", "*.qt", "*.qtl", "*.rpm", "*.smk", "*.wm",
               "*.wmv", "*.wob"]
    total_bA = 0
    total_numA = 0
    patternA = ["*.669", "*.aif", "*.aifc", "*.aiff", "*.amf", "*.asf", "*.au", "*.audiocd", "*.cda", "*.cdda", "*.far",
               "*.it", "*.itz", "*.lwv", "*.mid", "*.midi", "*.mp1", "*.mp2", "*.mp3", "*.mtm", "*.ogg", "*.ogm",
               "*.okt", "*.ra", "*.rmi", "*.snd", "*.stm", "*.stz", "*.ult", "*.voc", "*.wav", "*.wax", "*.wm", "*.wma",
               "*.wmv", "*.xm", "*.xmz"]
    total_bI = 0
    total_numI = 0
    patternI = ["*.ais", "*.bmp", "*.bw", "*.cdr", "*.cdt", "*.cgm", "*.cmx", "*.cpt", "*.dcx", "*.dib", "*.emf",
               "*.gbr", "*.gif", "*.gih", "*.ico", "*.iff", "*.ilbm", "*.jfif", "*.jif", "*.jpe", "*.jpeg", "*.jpg",
               "*.kdc", "*.lbm", "*.mac", "*.pat", "*.pcd", "*.pct", "*.pcx", "*.pic", "*.pict", "*.png", "*.pntg",
               "*.pix", "*.psd", "*.psp", "*.qti", "*.qtif", "*.rgb", "*.rgba", "*.rif", "*.rle", "*.sgi", "*.tga",
               "*.tif", "*.tiff", "*.wmf", "*.xcf"]
    total_bAP = 0
    total_numAP = 0
    patternAP = [".action", ".apk", ".app", ".bat", ".bin", ".cmd", ".com", ".command", ".cpl", ".csh", ".exe",
           ".gadget", ".inf", ".ins", ".inx", ".ipa", ".isu", ".job", ".jse", ".ksh", ".lnk", ".msc",
           ".msi", ".msp", ".mst", ".osx", ".out", ".paf", ".pif", ".prg", ".ps1", ".reg", "rgs", ".run",
           ".scr", ".sct", ".shb", ".shs", ".u3p", ".vb", ".vbe", ".widget", ".wiz"]

    for path, subdirs, files in os.walk(root):
        for name in files:
            for a in patternT:
                if fnmatch(name, a):
                    total_bT += (get_size(os.path.join(path, name)))
                    total_numT += 1
            for a in patternC:
                if fnmatch(name, a):
                    total_bC += (get_size(os.path.join(path, name)))
                    total_numC += 1
            for a in patternA:
                if fnmatch(name, a):
                    total_bA += (get_size(os.path.join(path, name)))
                    total_numA += 1
            for a in patternI:
                if fnmatch(name, a):
                    total_bI += (get_size(os.path.join(path, name)))
                    total_numI += 1
            for a in patternAP:
                if fnmatch(name, a):
                    total_bAP += (get_size(os.path.join(path, name)))
                    total_numAP += 1
            for a in patternV:
                if fnmatch(name, a):
                    total_bV += (get_size(os.path.join(path, name)))
                    total_numV += 1
                    
    print bytes2human(total_bT)
    print bytes2human(total_bC)
    print bytes2human(total_bA)
    print bytes2human(total_bI)
    print bytes2human(total_bAP)
    print bytes2human(total_bV)


def Datos_MapDisk_Archivo():
    
    get_file()
    
def grafica():
    py.sign_in('username', 'api_key')
    trace1 = Bar(
        x=[20],
        y=['Data'],
        marker=Marker(
            color='rgba(129, 216, 208, 0.6)',
            line=Line(
                color='rgba(color, 1.0)',
                width=2
            )
        ),
        name='Apps',
        orientation='h'
    )
    trace2 = Bar(
        x=[10],
        y=['Data'],
        marker=Marker(
            color='rgba(217, 130, 139, 0.6)',
            line=Line(
                color='rgba(color, 1.0)',
                width=2
            )
        ),
        name='Photos',
        orientation='h'
    )
    trace3 = Bar(
        x=[25],
        y=['Data'],
        marker=Marker(
            color='rgba(200, 162, 200, 0.6)',
            line=Line(
                color='rgba(color, 1.0)',
                width=2
            )
        ),
        name='Audio',
        orientation='h'
    )
    trace4 = Bar(
        x=[30],
        y=['Data'],
        marker=Marker(
            color='rgba(128, 140, 255, 0.6)',
            line=Line(
                color='rgba(color, 1.0)',
                width=2
            )
        ),
        name='Movies',
        orientation='h'
    )
    trace5 = Bar(
        x=[5],
        y=['Data'],
        marker=Marker(
            color='rgba(255, 243, 128, 0.6)',
            line=Line(
                color='rgba(color, 1.0)',
                width=2
            )
        ),
        name='Other',
        orientation='h'
    )
    trace6 = Bar(
        x=[5],
        y=['Data'],
        marker=Marker(
            color='rgba(255, 255, 255, 0.6)',
            line=Line(
                color='rgba(color, 1.0)',
                width=2
            )
        ),
        name='Available',
        orientation='h'
    )
    data = Data([trace1, trace2, trace3, trace4, trace5, trace6])
    layout = Layout(
        barmode='stack'
    )
    fig = Figure(data=data, layout=layout)
    py.plot(fig)

    
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
