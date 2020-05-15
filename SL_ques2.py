import numpy as np
import matplotlib.pyplot as plt
import math as m
from coeffs import *


		
e1=np.array([1,0])
e2=np.array([0,1])
p=np.array([2,1])
n=np.array([1,-1])
c=4
d=2*np.sqrt(3)
m=omat@n
lam=d/np.linalg.norm(m)
Q=p+lam*m
print(Q,2-np.sqrt(6))		
A_L =c/(n@e1)*e1
B_L =c/(n@e2)*e2
print(A_L)
print(B_L)
c1 = m@Q
X =(n,m)
cs = (c,c1)
Y=np.linalg.inv(X)@cs
x_AB_L = line_gen(A_L,B_L)
x_QY=line_gen(Q,Y)
plt.grid()
plt.plot(x_AB_L[0,:],x_AB_L[1,:],label ='$L$')
plt.plot(A_L[0],A_L[1],'o')
plt.text(A_L[0]*(1-0.1),A_L[1]*(1+0.1),'A_L')
plt.plot(B_L[0],B_L[1],'o')
plt.text(B_L[0]*(1 -0.2) ,B_L[1]*(1),'B_L')

plt.plot(x_QY[0,:],x_QY[1,:],label ='$QY$')
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]*(1-0.1),Q[1]*(1+0.1),'Q')
plt.plot(Y[0],Y[1],'o')
plt.text(Y[0] * (1 -0.2) ,Y[1]*(1),'Y')

plt.xlabel('$x$')
plt.xlabel('$y$')
plt.axis('equal')
plt.show()

		
