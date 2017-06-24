print "file2"
def fun():
	return "this is fun in file2.py"

def main():
	print "thi is file2"
	print "__name__--->",__name__

	print "some details"
	print fun()
	print "some other statements"
	print "end of the program"

if __name__ == "__main__":
	a=10
	b=20
	main()