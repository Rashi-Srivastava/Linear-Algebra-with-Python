

import numpy as np
from coeffs import *

for i in range(-10,10):
    A=[[i,5,-i],[-3*i,i,2],[1,1,1]]
    a=np.linalg.det(A)
    if int(a)==56:
        k=i
        Z=[[k,-3*k],[5,k],[-k,2]]
    
A=np.array(Z[0]);
B=np.array(Z[1]);
C=np.array(Z[2]);
        
p = np.zeros(2)

n1 = dir_vec(B,C)
p[0]=n1@A

n2 = dir_vec(C,A)
p[1]=n2@B


N=np.vstack((n1,n2))
H=np.linalg.inv(N)@p
print(H)
