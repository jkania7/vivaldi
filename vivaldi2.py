import numpy as np
import matplotlib.pyplot as plt

height = 10.0+3.0/8.0
width = 6.0+19.0/32.0
leftover = 2.0
R = 0.1*2.54
plt.rcParams["figure.figsize"] = [height, width]

z21 = -width/2.0
y21 = height - leftover
z11 = -0.05
y11 = 0.0
z1 = np.arange(z21, z11, 0.00001)

c11 = (y21-y11)/(np.exp(R*z21)-np.exp(R*z11))
c21 = (y11*np.exp(R*z21)-y21*np.exp(R*z11))/(np.exp(R*z21)- np.exp(R*z11))

y1 = c11*np.exp(R*z1)+c21

z22 = width/2.0
y22 = height - leftover
z12 = 0.05
y12 = 0.0
z2 = np.arange(z12, z22, 0.00001)

c12 = (y22-y12)/(np.exp(R*z22)-np.exp(R*z12))
c22 = (y12*np.exp(R*z22)-y22*np.exp(R*z12))/(np.exp(R*z22)- np.exp(R*z12))

y2 = c11*np.exp(-R*z2) + c21#-c12*np.exp(-R*z2)-c22


plt.figure(num=None, figsize=(height, width), dpi=100)
plt.plot(z1, y1, z2, y2)
plt.axis('equal')
plt.savefig('vivaldi2.png',dpi=300) 
plt.show()
