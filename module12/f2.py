"""
Doc string of the module
"""

print "program started"


def fun1(value1, value2=0):
    """
    Two add two numbers.
    :param: a: int
    :param:b:int, default value:0
    returns: int: Summation of a and b
    """
    return value1 + value2

print fun1(100, 200)
print "program ended"
