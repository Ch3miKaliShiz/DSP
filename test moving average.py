# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 17:35:29 2022

@author: rkatw
"""

import numpy as np

x = np.linspace(0,100,100)

M = 5
M_w = int(M/2)
i = 0
Y = []
while i < len(x):
    if i-M_w <0:
        selec = x[0:i+M_w]
        selec = np.repeat(np.insert(selec, 0, 0), np.abs(i-M_w))
    else:
        selec = x[(i-M_w): (i+M_w)]
    som = int(sum(selec))
    ma = som/M
    Y.append(ma)
    i +=1

print(Y)