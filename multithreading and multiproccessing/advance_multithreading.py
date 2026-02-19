# #multithreading with thread pool executor
# from concurrent.futures import ThreadPoolExecutor
# import time
# def print_number(number):
#     time.sleep(1)
#     return f"number:{number}"
# numbers=[1,2,3,4,5]
# with ThreadPoolExecutor(max_workers=3) as executor:
#     results=executor.map(print_number,numbers)
# for result in results:
#     print(result)

##multithreading with ProcessPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time
def sq_number(number    ):
    time.sleep(1)
    return f"Square:{number * number}"
numbers=[1,2,3,4,5]
if __name__=="__main__":
    with ProcessPoolExecutor (max_workers=3) as executor:
        results=executor.map(sq_number,numbers)
    for result in results:
        print(result)
