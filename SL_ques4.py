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

CD=np.array([1,-1])
C4=3

Aug2=(AD,CD)
print(Aug2)

cs2=np.array([C2,C4])
D=np.linalg.inv(Aug2)@cs2
print(D)

x_AB=line_gen(A,B)
x_AD=line_gen(A,D)
x_BC=line_gen(B,C)
x_CD=line_gen(C,D)
x_BD=line_gen(B,D)
x_AC=line_gen(A,C)


plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')


plt.grid() 
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.1), A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 - 0.1), C[1] * (1 + 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 - 0.2), D[1] * (1) , 'D')


plt.xlabel('$x$')
plt.ylabel('$y$')

plt.axis('equal')
plt.show()
