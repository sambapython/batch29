

def fun():
	return "this is fun in f2.py modified mofied again"

def main():
	print "thi is f2"
	print "__name__--->",__name__

	print "some details"
	print fun()
	print "some other statements"
	print "end of the program"

if __name__ == "__main__":
	def conf():
		return "this is confidential method."
	a=10
	b=20
	main()