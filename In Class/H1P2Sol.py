#!/usr/bin/env python
# H1P2 Solution
# Matt Stein to Create a 4x5 matrix of random numbers
# between 1 and 20

import numpy as np
import random
A=np.empty([4,5])
for i in range(0,4):
    for j in range(0,5):
        A[i,j]=random.random()*20
        #A[i,j]=random.randint(1,20)
print A
