import mod1
a1=10
b1=20
def fun(a,b):
	try:
		print "a=%s,b=%s"%(a,b)
		return a+b
	except Exception as err:
		print err
		return None
c=a1+b1
print mod1.fun()
print "c=",c
print fun(100,200)
try:
	for i in [1,3,-2,4,0,5]:
		print 10/i
except Exception as err:
	print err
print "program ended"