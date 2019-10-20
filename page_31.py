import  numpy as np
import matplotlib.pyplot as plt
from scipy import linalg
from scipy import integrate
from theta_new import theta_method

J=[10,11,12,13,14,15,16,18,20,26,30,40,60,80]

# %A:theta=0,miu=1/2
error1=[]
for i in range(len(J)):
    error1.append(np.log10(theta_method(0,J[i],0.5,0)))

plt.semilogx(J,error1,'-ok')


# %B1:theta=1/2 miu=1/2
#
error2=[]
for i in range(len(J)):
    error2.append(np.log10(theta_method(0.5,J[i],0.5,0)))
plt.semilogx(J,error2,'-xk')
# %B2: theta1/2 v=1/20
error4=[]
for i in range(len(J)):
    error4.append(np.log10(theta_method(0.5,J[i],0,0.05)))
plt.semilogx(J,error4,':xk')
# %C1: theta=1/2 miu=5
error3=[]
for i in range(len(J)):
    error3.append(np.log10(theta_method(0.5,J[i],5,0)))
plt.semilogx(J,error3,'-+k')
#
# %C2:theta=1/2 v=1/2

error5=[]
for i in range(len(J)):
    error5.append(np.log10(theta_method(0.5,J[i],0,0.5)))
plt.semilogx(J,error5,':+k')


# %D1:theta=1 miu=5
error6=[]
for i in range(len(J)):
    error6.append(np.log10(theta_method(1,J[i],5,0)))
plt.semilogx(J,error6,'-*k')
#
plt.ylabel(r'$log_{10}E^{n}$')
plt.xlabel('J')
#
# %D2:theta=1 v=0.5
error7=[]
for i in range(len(J)):
    error7.append(np.log10(theta_method(1,J[i],0,0.5)))
plt.semilogx(J,error7,'--*k')
plt.show()