# threads - block of code that executes
# simulate running multiple codes at once
# Ex: schedule threads in order of prioritization
# Or one thread per processor core
# make it sequential. Thread 1 executes while the others sleep

import threading
import time
import random

def execute_thread(i):
    print("Thread {} sleeps at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))
    rand_sleep_time = random.randint(1,4)
    time.sleep(rand_sleep_time)
    print("Thread {} stops sleeping at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))

for i in range(10):
    thread = threading.Thread(target=execute_thread, args=(i,))
    # requires i, in args to designate sequence
    thread.start()
    print("Active Threads :",threading.activeCount())
    print("Thread Objects :", threading.enumerate())

class CustThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        get_time(self.name)
        print("Thread", self.name, "Execution Ends")

def get_time(name):
    print("Tread {} sleeps at {}".format(name, time.strftime("%H:%M:%S", time.gmtime())))
    rand_sleep_time = random.randint(1,4)
    time.sleep(rand_sleep_time)

thread1 = CustThread("1")
thread2 = CustThread("2")

thread1.start()
thread2.start()

print("Thread 1 Alive? :", thread1.is_alive())
print("Thread 2 Alive? :", thread2.is_alive())