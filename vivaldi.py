import matplotlib.pyplot as plt
import numpy as np
import math

z1 = np.arange(-16.74/(2.0*2.54), -0.1/2.54, 0.001)
y1 = -47.285/2.54*np.exp(0.1*z1*2.54)+45.993/2.54
z2 = np.arange(0.1/2.54, 16.75/(2.0*2.54),0.001)
#y2 = -20.26/2.54*np.exp(-0.1*z2*2.54)+20.4645/2.54
y2 = -47.285/2.54*np.exp(-0.1*z2*2.54)+45.993/2.54
fig = plt.figure(num=None, figsize=(26.35/2.54,16.75/2.54), dpi=100)
plt.plot(z1,y1,z2,y2)
plt.savefig('Avivaldi.pdf')
plt.show()
