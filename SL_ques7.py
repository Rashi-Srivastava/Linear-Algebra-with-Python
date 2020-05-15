import numpy as np
import matplotlib.pyplot as plt
import math as m
from coeffs import *

A=np.array([0,0])
B=np.array([2,0])
C=np.array([2,2])
D=np.array([0,2])

Ang=-np.pi/6

T1= np.array([np.cos(Ang),-np.sin(Ang)])
T2= np.array([np.sin(Ang),np.cos(Ang)])

X=np.array([T1,T2])

L=A@X
M=B@X
N=C@X
O=D@X

E1=np.array([1,0])

Sum_F1=(A+B+C+D)@E1
Sum_F2=(L+M+N+O)@E1

print(Sum_F1)
print(Sum_F2)

x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)
x_LM = line_gen(L,M)
x_MN = line_gen(M,N)
x_NO = line_gen(N,O)
x_OL = line_gen(O,L)
plt.plot(x_AB[0,:],x_AB[1,:],label="$AB$")
plt.plot(x_BC[0,:],x_BC[1,:],label="$BC$")
plt.plot(x_CD[0,:],x_CD[1,:],label="$CD$")
plt.plot(x_DA[0,:],x_DA[1,:],label="$DA$")
plt.plot(x_LM[0,:],x_LM[1,:],label="$LM$")
plt.plot(x_MN[0,:],x_MN[1,:],label="$MN$")
plt.plot(x_NO[0,:],x_NO[1,:],label="$NO$")
plt.plot(x_OL[0,:],x_OL[1,:],label="$OL$")

plt.plot(A[0],A[1], 'o')
plt.text(A[1]*(1.01),A[1]*(1.01),'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*(1.01),B[1]*(1.02),'B')
plt.plot(C[0],C[1],'o')
plt.text(C[0]*(1.02),C[1]*(1.02), 'C')
plt.plot(D[0],D[1],'o')
plt.text(D[0]*(1.02),D[1]*(1.02),'D')

plt.plot(L[0],L[1],'o')
plt.text(L[0]*(1.01),L[1]*(1.01),'L')
plt.plot(M[0],M[1],'o')
plt.text(M[0]*(1.02),M[1]*(1.02), 'M')
plt.plot(N[0],N[1],'o')
plt.text(N[0]*(1.02),N[1]*(1.02),'N')
plt.plot(O[0],O[1],'o')
plt.text(O[0]*(1.01),O[1]*(1.01),'O')
plt.xlabel('$x$')
plt.ylabel('$y$')

plt.grid()
plt.axis('equal')

plt.show()



