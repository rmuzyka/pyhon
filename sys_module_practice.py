#!/usr/bin/python

import sys


# print '\n'.join(sys.modules.keys())

print sys.modules
print sys.version
print sys.version_info
print sys.getrecursionlimit()

print sys.argv
for i in range(len(sys.argv)):
    if i == 0:
        print "Function name: %s" % sys.argv[0]
    else:
        print "%d. argument: %s" % (i,sys.argv[i])
        
print '\n' 
x = 42
print x
def my_display(x):
    print "out: "
    print x
    
sys.displayhook = my_display
print x
x

# print sys.ps1

for i in (sys.stdin, sys.stdout, sys.stderr):
    print i
    


# while True:
#   # output to stdout:
#   print "Yet another iteration ..."
#   try:
#     # reading from sys.stdin (stop with Ctrl-D):
#     number = raw_input("Enter a number: ")
#   except EOFError:
#     print "\nciao"
#     break
#   else:
#     number = int(number)
#     if number == 0:
#       print >> sys.stderr, "0 has no inverse"
#     else:
#       print "inverse of %d is %f" % (number, 1.0/number) 

print sys.__displayhook__(None)
print sys.float_info.dig

print '\n'
for i in sys.argv:
    print i
    
print '\n'
print 'The PYTHONPATH is ', sys.path
for i in sys.path:
    print i
    
print '\n'
user_input = sys.stdin.readline
print("User input: " + user_input)