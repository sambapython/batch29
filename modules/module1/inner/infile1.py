print "infile"
def fun():
	return "this is fun in infile1.py"

def main():
	print "thi is infile1"
	print "__name__--->",__name__

	print "some details"
	print fun()
	print "some other statements"
	print "end of the program"

if __name__ == "__main__":
	a=10
	b=20
	main()