import  numpy as np
import matplotlib.pyplot as plt
from scipy import linalg
from scipy import integrate
from theta_new import theta_method

J=np.array([10,11,12,13,14,15,16,18,20,26,30,40,60,80])
delta_x=1/J
# %A:theta=0,miu=1/2                                         theta J miu v
delta_tA=0.5*delta_x**2
k1=1/(delta_x*delta_tA)
# %A:theta=0,miu=1/2
error1=[]
for i in range(len(J)):
    error1.append(np.log10(theta_method(0,J[i],0.5,0)))

plt.semilogx(k1,error1,'-ok')


# %B1:theta=1/2 miu=1/2
#
error2=[]
for i in range(len(J)):
    error2.append(np.log10(theta_method(0.5,J[i],0.5,0)))
plt.semilogx(k1,error2,'-xk')
# %B2: theta1/2 v=1/20

delta_tB2=0.05*delta_x
k4=1/(delta_x*delta_tB2)
error4=[]
for i in range(len(J)):
    error4.append(np.log10(theta_method(0.5,J[i],0,0.05)))
plt.semilogx(k4,error4,':xk')
# %C1: theta=1/2 miu=5
error3=[]
delta_tC1=5*delta_x**2
k3=1/(delta_x*delta_tC1)
for i in range(len(J)):
    error3.append(np.log10(theta_method(0.5,J[i],5,0)))
plt.semilogx(k3,error3,'-+k')
#
# %C2:theta=1/2 v=1/2
error5=[]
delta_tC2=0.5*delta_x
k5=1/(delta_x*delta_tC2)
for i in range(len(J)):
    error5.append(np.log10(theta_method(0.5,J[i],0,0.5)))
# end
plt.semilogx(k5,error5,':+k')
# %D1:theta=1 miu=5
error6=[]
delta_tD1=5*delta_x**2
k6=1/(delta_x*delta_tD1)
for i in range(len(J)):
    error6.append(np.log10(theta_method(1,J[i],5,0)))
# end
plt.semilogx(k5,error6,'-*k')
#
plt.ylabel(r'$log_{10}E^{n}$')
plt.xlabel('J')
#
# %D2:theta=1 v=0.5
error7=[]
delta_tD2=0.5*delta_x
k7=1/(delta_x*delta_tD2)
for i in range(len(J)):
    error7.append(np.log10(theta_method(1,J[i],0,0.5)))
# end
plt.semilogx(k7,error7,'--*k')

plt.show()