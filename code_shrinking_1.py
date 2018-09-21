# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 10:44:02 2018

@author: gydwo
"""

import random

y0 = random.randint(0,99)
x0 = random.randint(0,99)

agents = []
agents.append([y0,x0])


#printing the first value within the first list - y0
agents[0][0]
#print the second value of the first list - x0
agents[0][1]
#print both
print(agents)





agents.clear()


#finding a way to do the previous steps without defining
#y0 and x0
agents = []
agents.append([random.randint(0,99),random.randint(0,99)])

#adding y1 and x1 to the same list
agents.append([random.randint(0,99),random.randint(0,99)])
print(agents)

#finding the max coordinatres
#this only looks at the largest y coordinate first
print(max(agents))

#to be able to exploit the x value:
import operator
print(max(agents, key=operator.itemgetter(1)))

#operator.itemgetter(1) gets the second element

#to plot our agents
import matplotlib.pyplot as plt
plt.ylim(0, 99)
plt.xlim(0, 99)
plt.scatter(agents[0][1],agents[0][0])
plt.scatter(agents[1][1],agents[1][0])

x = max(agents, key=operator.itemgetter(1))[1]
y = max(agents, key=operator.itemgetter(0))[0]

plt.scatter(x,y, color='red')

plt.show()

#to make the most eastern point red
plt.ylim(0, 100)
plt.xlim(0, 100)
plt.scatter(agents[0][1],agents[0][0])
plt.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1))
plt.scatter(m[1],m[0], color='red')
plt.show()






