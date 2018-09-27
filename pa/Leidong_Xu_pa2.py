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
    print('This is ', str(i+1),'iteration')
    print('x is '+str(var))
    var = (var+1)-1
    print('(x+1-1) is '+ str(var))
    var = var/2.
    
"""
We can found that the smallest number could be showed in python float(double percision) is
1.1102230246251565e-16. The code printed is shown as following:
    
This is  53 iteration
x is 2.220446049250313e-16
(x+1-1) is 2.220446049250313e-16
This is  54 iteration
x is 1.1102230246251565e-16
(x+1-1) is 0.0
The reason why this happened is that the value of x is reaching machine epsilon 1.1102230246251565e-16
which is 2**(−53), and all the values are smaller than this number would be consider as 0
"""


###############################################################################
'Problem 2'
###############################################################################
import matplotlib.pyplot as plt
eps = np.finfo(float).eps

print('Here the Problem 2 start, there are not enough mem to repeat the gap at left top picture')

x0 = np.linspace(-0.99999,1,1000)
y0 = np.log(1.+ x0)/x0
plt.plot(x0,y0)
plt.xlim(-1,1)
plt.ylim(-1,3)
plt.grid()
plt.title('y = log(1+x)')
plt.show()

x1 = np.linspace(-5*eps,5*eps,1000)
y1 = np.log(1.+x1)/x1
plt.plot(x1,y1)
plt.grid()
plt.title('y = log(1+x)')
plt.show()
    
x2 = np.linspace(-0.99999,1,1000)
y2 = np.zeros_like(x2)
d2 = 1.+x2
for i in range(len(x2)):
    if x2[i]+1 == 1.:
        y2[i] = 1.0
    else:
        y2[i] = np.log(d2[i])/(d2[i]-1.)
plt.plot(x2,y2)
plt.xlim(-1,1)
plt.ylim(-1,3)
plt.grid()
plt.title('y = log(1+x)/[(1+x)-1')
plt.show()



x3 = np.linspace(-5*eps,5*eps,1000)
y3 = np.zeros_like(x3)
d3 = 1.+x3
for i in range(len(x2)):
    if x3[i]+1 == 1.:
        y3[i] = 1.0
    else:
        y3[i] = np.log(d3[i])/(d3[i]-1.)
plt.plot(x3,y3)
plt.title('y = log(1+x)/[(1+x)-1')
plt.grid()
plt.show()
