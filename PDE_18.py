import  numpy as np
import matplotlib.pyplot as plt

xf1 = np.linspace(0, 1, 51)
yf1 = np.polyval([0.5,0,0], xf1)
# plt.plot([0, 1], [0, 1])
plt.xlim((0, 1.05))
plt.ylim((0, 1))
plt.plot(xf1,yf1,label='$\mu$=0.5')
plt.plot(np.linspace(0, 1, 51),np.polyval([0.4,0,0], xf1),label='$\mu$=0.4')
plt.plot(np.linspace(0, 1, 51),np.polyval([0.2,0,0], xf1),label='$\mu$=0.2')
plt.plot(np.linspace(0, 1, 51),np.polyval([0.1,0,0], xf1),label='$\mu$=0.1')
plt.plot(np.linspace(0, 0.9, 51),np.polyval([1,0], np.linspace(0, 0.9, 51)),'g--',label=r'$\frac{\Delta t}{\Delta x}$=1')
plt.plot(np.linspace(0, 0.9, 51),np.polyval([0.5,0], np.linspace(0, 0.9, 51)),'--',label=r'$\frac{\Delta t}{\Delta x}$=0.5')
plt.legend(edgecolor='w')
plt.show()
