'''
Real-World example:multiprocessing for cpu-bound tasks
Scenario:factorial calculations
here,the factorial calculation that we are going to do will we will be doing for larger numbers.It involves significant computational work.
So with the help of multiprocessing, what we will do is that we will distribute the workload across multiple CPU cores improving the performance.

'''
import multiprocessing
import math
import sys
import time

#increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

#function to compute factorial of a given number
def computer_factorial(number):
    print(f"computing factorial of {number}")
    result=math.factorial(number)
    print(f"factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers=[50000,60000,700,500]
    start_time=time.time()

    #create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results=pool.map(computer_factorial,numbers)
    end_time=time.time()
    print(end_time-start_time)
