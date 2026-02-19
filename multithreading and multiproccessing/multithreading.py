#when to use multi threading:
#1)IO bound tasks:tasks that spend more time waiting for I/O operations(file operation,network request)\
#2)concurrent execution:when you want to improve the throughput of your application by performing multiple operations concurrently
import threading
import time
def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"number:{i}")
def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"letter:{letter}")

#create two threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)

t=time.time()
#start the thread
t1.start()
t2.start()

#wait for the threads to complete
t1.join()
t2.join()

print_numbers()
print_letters()
finished_time=time.time()-t
print(finished_time)