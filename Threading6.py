import time
import thread
def print_time( threadName,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName,time.ctime(time.time()))
try:
    thread.start_new_thread(print_time,("Thread-1",2, ) )
    thread.start_new_thread(print_time,("Thread-2",2, ) )
    thread.start_new_thread(print_time, ("Thread-3", 2,))
    thread.start_new_thread(print_time, ("Thread-4", 2,))
    thread.start_new_thread(print_time, ("Thread-5", 2,))
except:
    print "I am Bagu"
while 1:
   pass