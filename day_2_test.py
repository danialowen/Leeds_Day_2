# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 09:37:03 2018

@author: gydwo
"""

#Strings
a = 'dan'
b = ' owen'
print (a+b)

a[0]
a[2]



#Use of quotation marks '"\
c = "Dan's bike"
d = 'Dan is "awesome"'
e = "Dan's bike is \"awesome\""




#Tuples
w = (2,3,4)
print(type(w))




#Lists
g = [5,6,7,8]
print(len(g), g[1],g[-2])
g[2] = 33
print(g)




#Labels of lists
a = [1,2,3]
b = a
#Both a and b should be the same
print(a)
print(b)
#change first value of 'b' to a 100 and a will also change withouit
#explicitly telling it to
b[0] = 100
print(b)
print(a)





#Sub-list within a list
t = [1,2,3,4,5,6,7,8,9,10]
#sub-list includes the 3rd but not the 6th (3,4,5,6)
t[2:6]
#from the first character to the 5th - not include the 6th
t[:6]
#from the 5th index onwards
t[6:]
#from the 2nd character to the 8th in sets of 2
t[1:8:2]





#ranges
#create a range from 0-9
range(0,10)
list(range(0,10))
print(list(range(0,10))) 





#List within a list
q = [[1,2,3],[4,5,6,7,8],3]
print(len(q))
q[0]
#5th character of the 2nd sequence
q[1][4]






#Packing
#'divmod' gives the integer of the division and the remainder given as a tuple
divmod(9,2)

#the same as:
#divide as integer
9//2

#and the remainder
9%2




#unpacking (swap the variable values over)
f = 1
g = 2

f,g = g,f

#f is now 2, g is now 1

#long way around is
f = 1
g = 2

tmp = 1
f = g
g = tmp
f,g






