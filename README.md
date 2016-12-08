#Proyecto Final de Sistemas Operativos

##Integrantes:
```
Argel Torres Ramírez        - ArgelTorres
Katia Denisse Garcia Aviles - KatiaGarcia96
Leslie De Anda Zavala       - leslie827
Ricardo Abarca Zamora       - MuchoAbarca
```
##Primera entrega

```
1. Obtener la lista de procesos
2. Guardar los procesos en un archivo.txt
3. Hacer Map al disco
4. Crear un proceso
5. Matar un proceso
```

##Lo que sigue para el Avance 2

```
1.  La tabla de procesos en interfaz grafica 
    (se tiene que estar refrescando para que mostrar la lista sea lo mas parecido a la realidad)
2.  Capacidad de ordenar la tabla por cualquier columna.
3.  Capacidad de seleccionar un proceso de la tabla y matarlo.
4.  Grafica de distribución del disco duro:
    - Una por tipo de archivos
    - Otra por folders.
5.  Grafica "En Tiempo Real" de uso de procesador (Tipo Task Manager, Activity Monitor, etc).
6.  Grafica "En Tiempo Real" de uso de memoria.
7.  Minimo 10 GB de logs.
```
##Lo que sigue para la entrega final

```
1. Real time charts about process, memory, disk usage and threads (A premium version of Task Manager, Activity Monitor etc.)
2. Ability to create, kill or manage process and threads.
3.Ability to identify and manage memory
4.Ability to map the disk
5.Ability to clean the memory
6.Stats of application usage of memory, process, cpu, threads, etc.
7.Recommendation engine for better performance (30 GB logs)
```
#Checklist (Logrado hasta el 5 de Noviembre del 2016)
```
1.Tabla de proccesos en interfaz grafica
    -Refresh de la tabla de procesos (Realizado cada minuto)
    -Sort de la tabla por columna
    -Capacidad de seleccionar un proceso de la tabla y matarlo (delete de la tabla pero parece haber problemas con la manera en que se le hace kill)
La tabla de procesos por alguna razon no muestra la scroolbar para el tree view
2.Grafica de distribucion de disco duro:
    -Una por tipo de archivos
    -Otra por folders (posibles modificaciones)
3.Grafica "En tiempo real":
    -Procesador
    -Memoria
Ambas salen en una ventana aparte asi que se puede considerar que eso ya no suceda
4.Aproximadamente 10.3 GB de logs
```

##Algunas consideraciones adicionales
```
El proyecto hace uso de la libreria de Python para graficas conocida como Matplotlib, para obtenerlo se debe tener disponible esta libreria, en caso de no tenerla, en terminal ingresar sudo apt-get install python-matplotlib, adicionalmente se recomienda descargar numpy, el que igualmente, en terminal es sudo apt-get install python-numpy.
Se pueden combinar estas dos instrucciones escribiendo sudo apt-get install python-numpy python-matplotlib.

Adicionalmente, se usa de Tkinter que es una interfaz con el toolkit para GUI tk, mismo que viene incluido con la distribución de Python. Para usar Tkinter se debe de realizar una instalación, que se logra mediante el siguiente comando en terminal
sudo apt-get install python-tk

El proyecto utiliza el programa filelight el cual crea un mapdisk de las carpetas que se encuentran en el ordenador por lo cual es necesario ingresar el siguiente comando en la terminal:
sudo apt-get install filelight
```

#Todo lo relevante al proyecto esta dentro de: PF_SO/PycharmProjects/Proyecto/
