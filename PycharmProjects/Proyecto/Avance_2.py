import os
import logging
import plotly.plotly as py
from Tkinter import *
import ttk
from os import system
from time import sleep
from plotly.graph_objs import *
from logging import handler
from fnmatch import fnmatch
from multiprocessing import Process

root = '/'
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
                    
    total_bHT=bytes2human(total_bT)
    total_bHC=bytes2human(total_bC)
    total_bHA=bytes2human(total_bA)
    total_bHI=bytes2human(total_bI)
    total_bHAP=bytes2human(total_bAP)
    total_bHV=bytes2human(total_bV)

    grafica(total_bT,total_bC,total_bA,total_bI,total_bAP,total_bV,total_bHT,total_bHC,total_bHA,total_bHI,total_bHAP,total_bHV)

def Datos_MapDisk_Archivo():
    
    get_file()
    
def graficaArchivos(total_bT, total_bC, total_bA, total_bI, total_bAP, total_bV, total_bHT, total_bHC, total_bHA, total_bHI,total_bHAP, total_bHV):

        Nombres =  'Aplicaciones '+str(total_bHAP), 'Audio '+str(total_bHA), 'Video '+str(total_bHV), 'Comprimido '+str(total_bHC), 'Texto '+str(total_bHT), 'Imagenes '+str(total_bHI)
        tamano = [total_bAP, total_bA, total_bV, total_bC, total_bT, total_bI]
        colores = ['salmon', 'mediumturquoise', 'mediumpurple', 'yellowgreen', 'pink','lightseagreen']
        plt.pie(tamano, labels=Nombres, colors=colores, startangle=90)
        plt.axis('equal')
        plt.show()
        
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

def OnDoubleCLick(event):
    print ('its something')
    do_popup(event)

def do_popup(event):
    try:
        popup.tk_popup(event.x_root, event.y_root,0)
    finally:
        popup.grab_release()
def something():
    print('This is something')
def Cancel():
    print ('Nothing')
    
v0 = Tk()
v0.config(bg = "white")
v0.title("Task Monitor")
v0.geometry("800x500")
v0.update()
notebook = ttk.Notebook()
#notebook.pack(fill = BOTH, expand = YES)
notebook.pack()
widthw = 600 - 200
tree = ttk.Treeview()
tree2 = ttk.Treeview()
tree3 = ttk.Treeview()
popup = Menu(v0, tearoff = 0)
popup.add_command(label = "End task")
popup.add_command(label = "Sort", command = something)
sort_submenu = Menu(popup)
sort_submenu.add_command(label = "By User")
sort_submenu.add_command(label = "By CPU")
popup.add_cascade(label = "Sort", menu = sort_submenu)
popup.add_separator()
popup.add_command(label = "Quit", command = Cancel)
tree["columns"] = ("one", "two", "three", "four","five")
tree.column("one", width  = widthw/6)
tree.column("two", width = widthw/6)
tree.column("three", width = widthw/6)
tree.column("four", width = widthw/6)
tree.column("five", width = widthw/6)
#tree.column("five", width = 100)
tree.heading("one", text = "User" )
tree.heading("two", text = "Status")
tree.heading("three", text = "PID")
tree.heading("four", text = "CPU")
tree.heading("five", text = "Mem")
ysb = ttk.Scrollbar(orient = VERTICAL, command = tree.yview())
xsb = ttk.Scrollbar(orient = HORIZONTAL, command = tree.xview())
tree['yscroll'] = ysb.set
tree['xscroll'] = xsb.set
#tree.insert('',0, 'gallery', text = 'Applications')
tree.insert("", 0, text = "Applications", values=("0%", "145.6 MB", "0 MB/s", "O Mbps"))
tree.insert("", 0, text = "Applications", values=("0%", "145.6 MB", "0 MB/s", "O Mbps"))
#tree.pack(fill = BOTH,expand = YES)
tree.pack()
tree.bind("<Button-1>", OnDoubleCLick)
notebook.add(tree, text = 'Procesos')
notebook.add(tree2, text = 'CPU')
notebook.add(tree3, text = 'Mem')
v0.mainloop()
#import matplotlib.pyplot as plt
#plt.ion()
#class DynamicUpdate():
#    #Suppose we know the x range
#    min_x = 0
#    max_x = 10

#    def on_launch(self):
#        #Set up plot
#        self.figure, self.ax = plt.subplots()
#        self.lines, = self.ax.plot([],[], 'o')
#        #Autoscale on unknown axis and known lims on the other
#        self.ax.set_autoscaley_on(True)
        #self.ax.set_xlim(self.min_x, self.max_x)
        #Other stuff
#        self.ax.grid()


#    def on_running(self, xdata, ydata):
#        #Update data (with the new _and_ the old points)
#        self.lines.set_xdata(xdata)
#        self.lines.set_ydata(ydata)
        #Need both of these in order to rescale
#        self.ax.relim()
#        self.ax.autoscale_view()
        #We need to draw *and* flush
#        self.figure.canvas.draw()
#        self.figure.canvas.flush_events()

    #Example
#    def __call__(self):
#        import numpy as np
#        import time
#        self.on_launch()
#        xdata = []
#        ydata = []
#        for x in np.arange(0,1000,0.5):
#            xdata.append(x)
#            ydata.append(np.exp(-x**2)+10*np.exp(-(x-7)**2))
#            self.on_running(xdata, ydata)
#            time.sleep(1)
#        return xdata, ydata

#d = DynamicUpdate()
#d()
