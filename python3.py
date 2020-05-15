import numpy as np
import matplotlib.pyplot as plt
import math as m
from coeffs import *

e1=np.array([1,0])
e2=np.array([0,1])
P= np.array([-1,-2])
AB = np.array([1,-1])
C1=-1
AD = np.array([7,-1])
C2=5
cs=np.array([C1,C2])

Aug=(AB,AD)
print(Aug)
A = np.linalg.inv(Aug)@cs
print(A)

C=2*P-A
print(C)

BC=np.array([7,-1])
C3=-15

Aug1=(AB,BC)
print(Aug1)

cs1=np.array([C1,C3])

B=np.linalg.inv(Aug1)@cs1
print(B)
