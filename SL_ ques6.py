import numpy as np
import matplotlib.pyplot as plt
import math as m
from coeffs import*


X=np.array([1,1])
C1=2
n=np.array([1,1])
m=omat@n
print(m)
Y=np.array([1,-1])
C2=0
Aug=(X,Y)
print(Aug)
cs=np.array([C1,C2])
F=np.linalg.inv(Aug)@cs
print(F)
C=-2*F
print(C)
CF=dir_vec(C,F)
Y=np.linalg.norm(CF)
print(CF)
AB=CF*2/np.sqrt(3)
print(AB)
Area=1/2*AB*CF
print(Area)

