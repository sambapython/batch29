class c1:
	
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def op1(self):
		print ("op1 in c1")

class c2(c1):
	a123=100
	def __init__(self,a,b,c):
		self.c=c
		c1.__init__(self,a,b)
	def op2(self):
		print self
		c1.op1(self)
		print self.a123
	@classmethod
	def clm(cls):
		print cls
		print cls.a123
	@staticmethod
	def stat(a,b):
		print a
		print b

o2=c2(10,20,30)
print "o2",o2
print "c2",c2
print "calling op2 using o2"
o2.op2()
print "calling clm using o2"
o2.clm()
print "calling clm using c2"
c2.clm()
print "calling stat using c2"
c2.stat(100,200)
print "calling stat using o2"
o2.stat(1000,2000)
print "calling op2 using c2"
c2.op2()