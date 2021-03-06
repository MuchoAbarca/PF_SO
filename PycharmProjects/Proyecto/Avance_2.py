import os
import ttk
import time
import threading
from Tkinter import *
from time import sleep
from fnmatch import fnmatch
import numpy as np
import matplotlib.pyplot as plt
import psutil

pattern = []

class GrafProcesador():
    # minimo = 0
    # maximo = 10

    def Dibujar(self):
        self.figura, self.ax = plt.subplots()
        self.lineas, = self.ax.plot([], [])
        self.ax.set_autoscaley_on(True)
        # self.ax.set_xlim(self.minimo, self.maximo)
        self.ax.grid()

    def Corriendo(self, xdata, ydata):
        self.lineas.set_xdata(xdata)
        self.lineas.set_ydata(ydata)
        self.ax.relim()
        self.ax.autoscale_view()
        self.figura.canvas.draw()
        self.figura.canvas.flush_events()

    def __call__(self):
        self.Dibujar()
        xdata = []
        ydata = []
        for x in np.arange(0, 100, 0.5):
            ydat = psutil.cpu_percent(interval=1, percpu=False)
            xdata.append(x)
            ydata.append(ydat)
            self.Corriendo(xdata, ydata)
            time.sleep(1)
        return xdata, ydata


class GrafMemoria():

    def Dibujar(self):
        self.figura, self.ax = plt.subplots()
        self.lineas, = self.ax.plot([], [])
        self.ax.set_autoscaley_on(True)
        # self.ax.set_xlim(self.minimo, self.maximo)
        self.ax.grid()

    def Corriendo(self, xdata, ydata):
        self.lineas.set_xdata(xdata)
        self.lineas.set_ydata(ydata)
        self.ax.relim()
        self.ax.autoscale_view()
        self.figura.canvas.draw()
        self.figura.canvas.flush_events()

    def __call__(self):
        self.Dibujar()
        xdata = []
        ydata = []
        for x in np.arange(0, 100, 0.5):
            ydat = psutil.virtual_memory().percent
            xdata.append(x)
            ydata.append(ydat)
            self.Corriendo(xdata, ydata)
            time.sleep(1)
        return xdata, ydata


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
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


def Datos_MapDisk_Archivo():
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
                "*.okt", "*.ra", "*.rmi", "*.snd", "*.stm", "*.stz", "*.ult", "*.voc", "*.wav", "*.wax", "*.wm",
                "*.wma",
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

    rootA = '/home'
    for path, subdirs, files in os.walk(rootA):
        for name in files:
            for a in patternT:
                if fnmatch(name, a):
                    total_bT += (get_size(os.path.join(path, name)))
                    total_numT += 1
    for path, subdirs, files in os.walk(rootA):
        for name in files:
            for a in patternC:
                if fnmatch(name, a):
                    total_bC += (get_size(os.path.join(path, name)))
                    total_numC += 1
    for path, subdirs, files in os.walk(rootA):
        for name in files:
            for a in patternA:
                if fnmatch(name, a):
                    total_bA += (get_size(os.path.join(path, name)))
                    total_numA += 1
    for path, subdirs, files in os.walk(rootA):
        for name in files:
            for a in patternI:
                if fnmatch(name, a):
                    total_bI += (get_size(os.path.join(path, name)))
                    total_numI += 1
    for path, subdirs, files in os.walk(rootA):
        for name in files:
            for a in patternAP:
                if fnmatch(name, a):
                    total_bAP += (get_size(os.path.join(path, name)))
                    total_numAP += 1
    for path, subdirs, files in os.walk(rootA):
        for name in files:
            for a in patternV:
                if fnmatch(name, a):
                    total_bV += (get_size(os.path.join(path, name)))
                    total_numV += 1
    total_bFree = psutil.virtual_memory().free
    total_bHFree = bytes2human(total_bFree)
    total_bHT = bytes2human(total_bT)
    total_bHC = bytes2human(total_bC)
    total_bHA = bytes2human(total_bA)
    total_bHI = bytes2human(total_bI)
    total_bHAP = bytes2human(total_bAP)
    total_bHV = bytes2human(total_bV)

    Nombres = ['Aplicaciones ' + str(total_bHAP), 'Audio ' + str(total_bHA), 'Video ' + str(total_bHV),
               'Comprimido ' + str(total_bHC), 'Texto ' + str(total_bHT), 'Imagenes ' + str(total_bHI),
               'Libre ' + str(total_bHFree)]
    tamano = [total_bAP, total_bA, total_bV, total_bC, total_bT, total_bI, total_bFree]
    colores = ['salmon', 'mediumturquoise', 'mediumpurple', 'yellowgreen', 'pink', 'lightseagreen', 'lightgray']
    plt.pie(tamano, labels=Nombres, colors=colores, startangle=90)
    plt.axis('equal')
    plt.show()


def Datos_MapDisk_Carpeta():
    os.system('nohup filelight "/home"')

def guarda_procesos():
    os.system("ps axo 'User: %u | "
              "Process: %c | "
              "CPU_Percentage: %C | "
              "VirtualMemory: %z | "
              "Tiempo: %x' --sort -vsize >> Procesos.log")


def OnDoubleCLick(event):
    print ('its something')
    do_popup(event)


def do_popup(event):
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        popup.grab_release()


def something():
    print('This is something')


def Cancel():
    print ('Nothing')


def TabChange(event):
    print (notebook.select())
    print (notebook.index(notebook.select()))
    if notebook.index(notebook.select()) == 0:
        print ('Case 1')
    elif notebook.index(notebook.select()) == 1:
        print ('Case 2')
        # Grafica procesador
        plt.ion()
        x = GrafProcesador()
        x()

    elif notebook.index(notebook.select()) == 2:
        print ('Case 3')
        # Grafica memoria
        plt.ion()
        y = GrafMemoria()
        y()

    #elif notebook.index(notebook.select()) == 3:
    #    print('Case 4')
    #    #Grafica de uso de disco
    #    plt.ion()
    #    z=GrafDisk_usage()
    #    z()
    elif notebook.index(notebook.select()) == 3:
        Datos_MapDisk_Archivo()
        print('Case 5')
    elif notebook.index(notebook.select()) == 4:
        Datos_MapDisk_Carpeta()
        print('Case 6')
    else:
        sys.exit(0)


def TaskEnder():
    print ('Delete')
    selected_item = tree.selection()[0]
    print (selected_item)
    curItem = tree.focus()
    print  tree.item(curItem)
    dic = tree.item(curItem)
    print (dic['values'][2])
    tree.delete(selected_item)
    # print(os.kill(dic['values'][2],0))
    print(int(dic['values'][2]) + 1)
    os.kill(int(dic['values'][2]), 0)
    print('first os kill complete')
    try:
        os.kill(int(dic['values'][2]), 0)
        raise Exception("""wasn't able to kill the process
                              HINT:use signal.SIGKILL or signal.SIGABORT""")
    except OSError as ex:
        print('other error')


def SortPID():
    process_names = [proc.name() for proc in psutil.process_iter()]
    process_ids = [proc.pid for proc in psutil.process_iter()]
    process_cpu = [proc.cpu_percent() for proc in psutil.process_iter()]
    process_mem = [proc.memory_percent() for proc in psutil.process_iter()]
    process_status = []
    process_thread = []
    process_user = [proc.username() for proc in psutil.process_iter()]
    num2 = 0
    for index in enumerate(process_ids):
        p = psutil.Process(process_ids[num2])
        process_status.append(p.status())
        process_thread.append(p.num_threads())
        num2 += 1
    process_ids, process_cpu, process_mem, process_names, process_status, process_user = zip(
        *sorted(zip(process_ids, process_cpu, process_mem, process_names, process_status, process_user)))
    tree.delete(*tree.get_children())
    num = 0
    for index in enumerate(process_mem):
        tree.insert("", 0, text=process_names[num],
                    values=(
                        process_user[num], process_status[num], process_ids[num], process_cpu[num], process_mem[num]))
        num += 1
    textthread_label.set('Total number of threads:' + str(sum(process_thread)))


def Sortmem():
    process_names = [proc.name() for proc in psutil.process_iter()]
    process_ids = [proc.pid for proc in psutil.process_iter()]
    process_cpu = [proc.cpu_percent() for proc in psutil.process_iter()]
    process_mem = [proc.memory_percent() for proc in psutil.process_iter()]
    process_status = []
    process_thread = []
    process_user = [proc.username() for proc in psutil.process_iter()]
    num2 = 0
    for index in enumerate(process_ids):
        p = psutil.Process(process_ids[num2])
        process_status.append(p.status())
        process_thread.append(p.num_threads())
        num2 += 1
    process_mem, process_ids, process_cpu, process_names, process_status, process_user = zip(
        *sorted(zip(process_mem, process_ids, process_cpu, process_names, process_status, process_user)))
    tree.delete(*tree.get_children())
    num = 0
    for index in enumerate(process_mem):
        tree.insert("", 0, text=process_names[num],
                    values=(
                        process_user[num], process_status[num], process_ids[num], process_cpu[num], process_mem[num]))
        num += 1
    textthread_label.set('Total number of threads:' + str(sum(process_thread)))


def SortCPU():
    process_names = [proc.name() for proc in psutil.process_iter()]
    process_ids = [proc.pid for proc in psutil.process_iter()]
    process_cpu = [proc.cpu_percent() for proc in psutil.process_iter()]
    process_mem = [proc.memory_percent() for proc in psutil.process_iter()]
    process_status = []
    process_thread = []
    process_user = [proc.username() for proc in psutil.process_iter()]
    num2 = 0
    for index in enumerate(process_ids):
        p = psutil.Process(process_ids[num2])
        process_status.append(p.status())
        process_thread.append(p.num_threads())
        num2 += 1
    process_cpu, process_mem, process_ids, process_names, process_status, process_user = zip(
        *sorted(zip(process_cpu, process_mem, process_ids, process_names, process_status, process_user)))
    tree.delete(*tree.get_children())
    num = 0
    for index in enumerate(process_mem):
        tree.insert("", 0, text=process_names[num],
                    values=(
                        process_user[num], process_status[num], process_ids[num], process_cpu[num], process_mem[num]))
        num += 1
    textthread_label.set('Total number of threads:' + str(sum(process_thread)))


def Refreshtree():
    threading.Timer(15, Refreshtree).start()
    print ('start')
    tree.delete(*tree.get_children())
    process_names = [proc.name() for proc in psutil.process_iter()]
    process_ids = [proc.pid for proc in psutil.process_iter()]
    process_cpu = [proc.cpu_percent() for proc in psutil.process_iter()]
    process_mem = [proc.memory_percent() for proc in psutil.process_iter()]
    process_status = []
    process_thread = []
    process_user = [proc.username() for proc in psutil.process_iter()]
    num2 = 0
    for index in enumerate(process_ids):
        p = psutil.Process(process_ids[num2])
        process_status.append(p.status())
        process_thread.append(p.num_threads())
        num2 += 1
    num = 0
    for index in enumerate(process_mem):
        tree.insert("", 0, text=process_names[num],
                    values=(
                        process_user[num], process_status[num], process_ids[num], process_cpu[num], process_mem[num]))
        num += 1
    textthread_label.set('Total number of threads:' + str(sum(process_thread)))

def clean_mem():
    os.system(" sudo sh -c 'echo 3 >/proc/sys/vm/drop_caches'")
def deact_swap():
    os.system(" sudo swapoff -a")
def act_swap():
    os.system(" sudo swapon -a")
    
v0 = Tk()
v0.config(bg="white")
v0.title("Task Monitor")
v0.geometry("800x500")
v0.update()
notebook = ttk.Notebook()
notebook.pack(fill=BOTH, expand=YES)
# notebook.pack()
widthw = 600 - 200
process_names = [proc.name() for proc in psutil.process_iter()]
process_ids = [proc.pid for proc in psutil.process_iter()]
process_cpu = [proc.cpu_percent() for proc in psutil.process_iter()]
process_mem = [proc.memory_percent() for proc in psutil.process_iter()]
process_status = []
process_thread = []
process_user = [proc.username() for proc in psutil.process_iter()]
num2 = 0
for index in enumerate(process_ids):
    p = psutil.Process(process_ids[num2])
    process_status.append(p.status())
    process_thread.append(p.num_threads())
    num2 += 1

tree = ttk.Treeview()
textthread_label = StringVar()
textthread_label.set('Total number of threads:' + str(sum(process_thread)))
thread_label = Label(textvariable=textthread_label)
thread_label.pack()
CPUframe = ttk.Frame()
Memframe = ttk.Frame()
# Pestanas para el MapDisk
MDA = ttk.Frame()
MDC = ttk.Frame()
EXIT = ttk.Frame()

popup = Menu(v0, tearoff=0)
popup.add_command(label="End task", command=TaskEnder)
# popup.add_command(label = "Sort", command = something)
# popup.add_command(label = "Sort")
sort_submenu = Menu(popup)
sort_submenu.add_command(label="By PID", command=SortPID)
sort_submenu.add_command(label="By CPU", command=SortCPU)
sort_submenu.add_command(label="By mem", command=Sortmem)
popup.add_cascade(label="Sort", menu=sort_submenu)
popup.add_separator()
popup.add_command(label="Quit", command=Cancel)
tree["columns"] = ("one", "two", "three", "four", "five")
tree.column("one", width=widthw / 6)
tree.column("two", width=widthw / 6)
tree.column("three", width=widthw / 6)
tree.column("four", width=widthw / 6)
tree.column("five", width=widthw / 6)
# tree.column("five", width = 100)
tree.heading("one", text="User")
tree.heading("two", text="Status")
tree.heading("three", text="PID")
tree.heading("four", text="CPU")
tree.heading("five", text="Mem")
ysb = ttk.Scrollbar(orient=VERTICAL, command=tree.yview())
xsb = ttk.Scrollbar(orient=HORIZONTAL, command=tree.xview())
tree['yscroll'] = ysb.set
tree['xscroll'] = xsb.set
# tree.insert('',0, 'gallery', text = 'Applications')
# tree.insert("", 0, text = "Applications", values=("0%", "145.6 MB", "0 MB/s", "O Mbps"))
# tree.insert("", 0, text = "Applications", values=("0%", "145.6 MB", "0 MB/s", "O Mbps"))
num = 0
for index in enumerate(process_mem):
    tree.insert("", 0, text=process_names[num],
                values=(process_user[num], process_status[num], process_ids[num], process_cpu[num], process_mem[num]))
    num += 1

tree.pack(fill=BOTH, expand=YES)
# tree.pack()
tree.bind("<Button-1>", OnDoubleCLick)
notebook.add(tree, text='Procesos')
notebook.add(CPUframe, text='CPU')
notebook.add(Memframe, text='Mem')
# agregar las pestanas del mapdisk a la ventana
notebook.add(MDA, text='MapDisk de Archivos')
notebook.add(MDC, text='MapDisk de Carpetas')

notebook.add(EXIT, text='Salir')

button_mem = Button(Memframe, text = "Free Cache", command = clean_mem)
button_mem.pack()
button_actswap = Button(Memframe, text = "Activate Swap", command = act_swap)
button_actswap.pack()
button_deactswap = Button(Memframe, text = "Deactivate Swap", command = deact_swap)
button_deactswap.pack()

# Detectar el cambio de tab
notebook.bind("<ButtonRelease-1>", TabChange)
v0.mainloop()
