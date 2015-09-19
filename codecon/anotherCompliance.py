#Problem        : Yet Another Compliance Problem
#Language       : Python
#Compiled Using : py_compile
#Version        : Python 2.7.8
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

from __future__ import print_function
import sys
import math

data = sys.stdin.readlines()

for line in data :
    line = line.replace("\n","")
    
    alpha = {}
    for c in line:
        if c not in alpha: alpha[c] = 1
        else: alpha[c] += 1
    
    odds = 0
    for freq in alpha.values():
        if freq % 2 == 1:
            odds += 1
    if odds > 1:
        print(0) 
    else:
        n = len(line)
        top = math.factorial(n/2)
        for freq in alpha.values():
            top /= math.factorial(freq/2)
        print(top)
    