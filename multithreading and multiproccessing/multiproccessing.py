#processes that run in parallel
#CPU-BOUND TASKS->task that are heavy on cpu usage (eg-mathematical computation)
#parallel execution->multiple cores of cpu

import multiprocessing
import time
def sq_number():
    for i in range(5):
        time.sleep(1)
        print(f"Square:{i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube:{i*i*i}")

if __name__=="__main__":
    #create two processes
    p1=multiprocessing.Process(target=sq_number)
    p2=multiprocessing.Process(target=cube_numbers)
    t=time.time()
    #start the process
    p1.start()
    p2.start()

    #wait for process to complete
    p1.join()
    p2.join()
    finished_time=time.time()-t
    print(finished_time)

