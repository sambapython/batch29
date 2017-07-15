import logging
import time
from app1 import fun1
logging.basicConfig(filename="log.txt", level=logging.DEBUG,
	format="%(asctime)s->%(levelname)s==>>%(message)s")
fun1(10,200)
def fun(a,b):
	c=a+b
	logging.debug('cost price: %s'%c)
	time.sleep(2)
logging.info("Function started:%s"%time.time())
fun(10,20)
logging.info("Function ended:%s"%time.time())
logging.debug("DEBUG statement")
logging.warn("WARNING statement")
logging.exception("Exception  statement")
logging.error("Error statement")