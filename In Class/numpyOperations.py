#!/usr/bin/env python
# use the numpy library

import numpy as np

A=np.ones([4,5])
for i in range(0,4):
    for j in range(0,5):
        A[i,j]=i*j

print A
print np.round(np.sin(A*np.pi/2))

    

