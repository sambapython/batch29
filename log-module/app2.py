import pdb
print "program started"
a=10
b=20
c=a+b
def fun(c1,c2):
	d1=0
	try:
		print "c1=",c1
		print "c2=",c2
		d1=c1+c2
	except Exception as err:
		print err
	return d1

print "c=",c
s=0 #10+2.5+1.4+2.5+1.4+1.2
for i in [1,4,7,4,7,8]:
	print "iteration started"
	res = 10/float(i)
	s=s+res
	print "iteration ended"
print "s=",s
for i in [1,4,7,0,4,7,8]:
	try:
		print "iteration started"
		print 10/i
		print "iteration ended"
	except Exception as err:
		print err
pdb.set_trace()
fun(100,200)
print "other statements in program"
print "program ended"
