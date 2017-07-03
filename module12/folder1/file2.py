"""
Doc string of the module
"""

print "file2"
def fun1(value1, value2=0):
    """
    Two add two numbers.
    :param: a: int
    :param:b:int, default value:0
    returns: int: Summation of a and b
    """
    return value1 + value1

def main():
    """
    this is main method.
    """
    print "program started"
    fun1(10, 20)
    print "program ended."

if __name__ == "__main__":
    main()
