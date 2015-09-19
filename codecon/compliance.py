#Problem        : A Compliance Problem
#Language       : Python
#Compiled Using : py_compile
#Version        : Python 2.7.8
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

from __future__ import print_function
import sys

data = sys.stdin.readlines()

for line in data :
    canPass = True
    
    alpha = {}
    line = line.replace("\n","").strip()
    for c in line:
        if c not in alpha:
            alpha[c] = 1
        else:
            alpha[c] += 1
    
    odd = 0
    for c,cnt in alpha.items():
        if cnt % 2 != 0:
            odd += 1
            
    if odd > 1:
        canPass = False
            
    if canPass == True:
        print("yes")
    else:
        print("no")