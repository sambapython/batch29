import logging
d={"name":"Anil",'age':23,"sal":"3.34L"}
print "Name: {0}, Age: {1}, sal:{2}".format(d.get('name'),d.get('age'),d.get("sal"))
print "Name: %(name)s, Age: %(age)s, Sal: %(sal)s"%d

def fun1(a,b):
	logging.info("A=%s"%a)
	logging.info("B=%s"%b)
	c=a+b
	logging.debug("VALUE=%s"%c)
	return c

