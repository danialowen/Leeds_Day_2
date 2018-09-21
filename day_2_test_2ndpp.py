# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 11:53:39 2018

@author: gydwo
"""

#Functions

def squared(x):
    x_squared = x**2
    return x_squared
#e.g. squared(4) will give you 16


#x is only defined within the function, and not outside

def double_it(z):
    return 2*z
#e.g. double_it(3) will give you 6


def pythagoras(a,b):
    c_squared = a**2+b**2
    return c_squared**0.5, c_squared
#e.g. pythagoras (3,4) will give you (5,25) - answer of 5


def show_me():
    print("dan")
    return None 







#numpy arrays
#numpy arrays are mutable, like lists
#numpy has arange which is like range but for real numbers 

import numpy as np

a = np.array([[1,2],[3,4]])
print(a)
print(np.ndim(a))
#np.dim is the number of lists
print(np.shape(a))
print(np.size(a))
print(a.min())
print(a.sum())



b = np.array(range(20))
print(b.reshape(4,5))


c = np.zeros([4,3])
d = np.ones ([2,5])
print(c)
print(d)
e = np.eye(5)
print(e)

print(np.arange(1.1,2.5,0.2))

#if you want to know whast space to be able to make 150 entries in sequence
q = np.linspace(1.0,20.0,150)
print(q)

a = np.arange(0,15)
print(a[3:6])

a = np.array(range(20))
b = b.reshape(4,5)
print(b)
#print a single row
print(b[1,:])
#print a single collumn
print(b[:,1])


#b*2 will mulitply each element by 2 and not repeat the sequence twice
b*2











#Control FLows


#if
x = 11

if x<10:
    print('danial')
else:
    print('owen')


#while

n = 10
tr = 0

#good for when you don't know how many times it will take
while n>0:
    tr+= n 
    n -= 1
print(tr)

#good for when you do know how many times it will take
for _ in range(5):
    print('dan')
    
for a in [4,6,2,4,8]:
    for b in "dan":
        print(a,b)
