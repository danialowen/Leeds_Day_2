# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:27:28 2018

@author: gydwo
"""

import random
import operator
import matplotlib.pyplot

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.

# j is the number of iterations, i.e. we flip the coin 100
# times and it moves once in each direction each time. instead of
# flipping the coin once and it moves in one direction 100 paces 

# i is the range of agents, which is 10 coordinates

# the first section is [i][0] which determines the y coords and decides
# whether it moves up or down

# the second section is [i][1] which determines the x coords and decides
# whether it moves left or right

# the %100 divides it by a hundered and ensures the point stays on grid
# e.g. 100x100 grid. point is 103, divided by 100 and remainder is 3
# thus, a valuer of 3 ensures it re-enters the grid on other side 



for j in range(num_of_iterations):
    
    for i in range(num_of_agents):
        
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
            
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
            

#Pythagoras code for calculating the distance
# answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
# print(answer)


#plot
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()