#Problem        : Base Arithmetic
#Language       : Python
#Compiled Using : py_compile
#Version        : Python 2.7.8
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

from __future__ import print_function
import sys

data = sys.stdin.readlines()

line1 = data[0].replace("\n","").strip()
line2 = data[1].replace("\n","").strip()

bases=[0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

base1 = 0
base2 = 0

currBase = 1
for b in bases:
    if str(b) in line1:
        base1 = currBase
    if str(b) in line2:
        base2 = currBase
    currBase += 1

print(int(line1,base1) + int(line2,base2))