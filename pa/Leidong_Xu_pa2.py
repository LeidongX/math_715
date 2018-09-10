"""
Applied math I programming assignment 2
"""

import numpy as np

"""
Problem 1 
For this program, initialize a variable to 1.0, then run a for loop for, say, 1200 iterations, and have
it print the following three numbers: the iteration number, x, and (x + 1) − 1. Finish the loop by
updating x to x/2
"""

var = 1.0
for i in range(1200):

    print('This is', str(i+1),'iteration')
    print('var is'+str(var))
    var = (var+1)-1
    print('var +1 -1 is'+ str(var))
#    var = var/2.
    
