import numpy as np
import matplotlib.pyplot as plt
from coeffs import*

K1=2
K2=-23/5
A=np.array([K1,-3*K1])
B=np.array([5,K1])
C=np.array([-K1,2])
m1=dir_vec(B,C)
m2=dir_vec(A,C)
print(m1)
print(m2)
n1=omat@m1
print(n1)
n2=omat@m2
print(n2)
Aug=(n1,n2)
print(Aug)
c1=m1@A
c2=m2@B
print(c1)
print(c2)
D=(c1,c2)
print(D)
X=np.linalg.inv(Aug)@D
print(X)

A=np.array([K2,-3*K2])
B=np.array([5,K2])
C=np.array([-K2,2])
m3=dir_vec(B,C)
m4=dir_vec(A,C)
print(m3)
print(m4)
n3=omat@m3
print(n3)
n4=omat@m4
print(n4)
Aug1=(n3,n4)
print(Aug1)
c3=m3@A
c4=m4@B
print(c3)
print(c4)
E=(c3,c4)
print(E)
Y=np.linalg.inv(Aug1)@E
print(Y)

