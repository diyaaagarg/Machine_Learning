import logging

#logging setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d%H:%M:%S',
    #handlers->form of lists
    #streamHandler ->stream handler is one method which will be responsible in putting all the logs information inside this particular file  
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ],
)
logger=logging.getLogger("Arithmetic App")
def add(a,b):
    result=a+b
    logger.debug(f"adding {a}+{b}={result}")
    return result

def subtract(a,b):
    result=a-b
    logger.debug(f"adding {a}-{b}={result}")
    return result

def multiply(a,b):
    result=a*b
    logger.debug(f"adding {a}*{b}={result}")
    return result

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"dividing {a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("division by 0")
        return None
    
add(2,3)
subtract(5,2)
multiply(2,3)
divide(10,5)