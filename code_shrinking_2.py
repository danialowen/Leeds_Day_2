# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:03:20 2018

@author: gydwo
"""

import random

#start of practical 2

#define agents
agents = []

#set the number of agents
num_of_agents = 10
#number of changes in arbitary 
number_of_iterations = 100

#The for-loop to create the ten agents
#for i in range(num_of_agents):
#    agents.append([random.randint(0,100),random.randint(0,100)])
#
#if random.random() < 0.5:
#    agents[0][0] += 1
#else:
#    agents[0][0] -= 1
#
#if random.random() < 0.5:
#    agents[0][1] += 1
#else:
#    agents[0][1] -= 1
#
#if random.random() < 0.5:
#    agents[0][0] += 1
#else:
#    agents[0][0] -= 1
#
#if random.random() < 0.5:
#   agents[0][1] += 1
#else:
#    agents[0][1] -= 1

  
    
#create shorter for-loop and to move twice

for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

#instead of writing the for-loop for each agent 10 times, 
#by writing 'i' it changes each agent


#for i in range(num_of_agents):  
 #   if random.random() < 0.5:
  #      agents[i][0] += 1
   #     agents[i][1] += 1
   # else:
   #     agents[i][0] -= 1
   #     agents[i][1] -= 1
   # if random.random() < 0.5:
   #     agents[i][0] += 1
   #     agents[i][1] += 1
   # else:
   #     agents[i][0] -= 1
   #     agents[i][1] -= 1
        


        
#create a new loop considering the no. of iterations
for i in range(num_of_agents):  
    if random.random() < 0.5:
        agents[i][0] += number_of_iterations
        agents[i][1] += number_of_iterations
    else:
        agents[i][0] -= number_of_iterations
        agents[i][1] -= number_of_iterations    
        
#plot
import matplotlib.pyplot 
matplotlib.pyplot.ylim(-200, 400)
matplotlib.pyplot.xlim(-200, 400)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()
      
#Blur
for i in (range(1,98)):
    datarow = []
    for j in (range(1,98)):
