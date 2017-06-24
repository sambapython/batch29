
print "file1"
#from inner import infile1
def fun():
	return "this is fun in file1.py"

def main():
	print "thi is file1"
	print "__name__--->",__name__

	print "some details"
	print fun()
	print "some other statements"
	print "end of the program"

if __name__ == "__main__":
	#print infile1.fun()
	a=10
	b=20
	main()