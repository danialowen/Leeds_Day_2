# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 11:07:34 2018

@author: gydwo
"""

import random

#finding a way to do the previous steps without defining
#y0 and x0
agents = []
agents.append([random.randint(0,99),random.randint(0,99)])

#adding y1 and x1 to the same list
agents.append([random.randint(0,99),random.randint(0,99)])
print(agents)
