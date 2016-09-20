import psutil
import os

def usoDeMemoria():
    procesin = psutil.Process(os.getpid())
    cuanto = procesin.memoria_utilizada()[0]/float(2**20)
    return cuanto

while True:
    print usoDeMemoria()


def PorcentajeEnCPU():

    process = psutil.Process(os.getpid())
    porcentaje = process.cpu_times(interval =1)
    return porcentaje
while True:
    print PorcentajeEnCPU()


for proceso in psutil.listaDeProcesos():
    numerin = psutil.Process(proceso)

print proceso.name, proceso.cdmline, proceso.pid

