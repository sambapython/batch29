'''
print fun()
'''
'''
import f1
print f1.fun()
'''
'''
import f2
'''
"""
from f2 import fun
"""
"""
from f2 import fuin,fun1
"""
"""
from f2 import fun,a,b
print "*"*60
print fun()
"""
'''
import f2
print "*"*60
print f2.fun()
'''
'''
import f3
print f3.main()
print f3.fun()
print f3.conf()
print f3.a
'''
"""
import module1
"""
"""
from module1 import file1
"""
"""
import module1
print module1.file1.fun()
print module1.file2.fun()
"""
'''
from module1 import file1,file2
print file1.fun()
print file2.fun()
'''
'''
import module1
print module1.file1.fun()
print module1.file2.fun()
'''
'''
from module1 import file1
print file1.fun()
print module1.file2.fun()
'''
'''
from module1.inner import infile1
print infile1.fun()
'''
'''
from module1 import inner
print inner.infile1.fun()
'''
import module1
print module1.infile1.fun()