import numpy as np
import matplotlib.pyplot as plt
delta_t = delta_x =0.02
def upwindmethod(delta_x,delta_t,tf):
    x = np.linspace(0,1,int(1/delta_x+1))
    x1=np.copy(x)
    x[:] = 0
    # for i in range(int(1/delta_x+1)):
    #     if x[i]>=0.2 and x<=0.4:
    #         x[i]=1
    #     else: x[i]=0
    x[int(0.2/delta_x+1):int(0.4/delta_x+1)] = 1

    a = (1+x1**2)/(1+2*x1**2+x1**4)
    v =  a * delta_t/delta_x
    ui = np.linspace(0,1,int(1/delta_x+1))
    ui[:]= x
    u = np.linspace(0,1,int(1/delta_x+1))
    u = x
    # print(x)
    for i  in range(1,int(tf/delta_x)):
        for j in range(2,int(1/delta_x)):
            u[j]=(1-v[j]**2)*ui[j]+0.5*v[j]*(1+v[j])*ui[j-1]-0.5*v[j]*(1-v[j])*ui[j+1]

        a = (1+x1**2)/(1+2*x1*i*delta_t+2*x1**2+x1**4)
        v =  a * delta_t/delta_x
        ui[:]=u



    y1 = x1 - tf/(1+x1**2)
    y = np.zeros(int(1/delta_x+1))
    for i in range(int(1/delta_x+1)):
        if y1[i]>0.2 and y1[i]<=0.4:
            y[i]=1
        else: y[i]=0
    # print(y)

    return ui,y
# upwindmethod(0.02,0.02,1)
# print(x)
# plt.plot(x)
plt.subplot(421)
plt.plot(upwindmethod(0.02,0.02,0)[0], 'o-',markersize=2.5)
plt.plot(upwindmethod(0.02,0.02,0)[1], '--')
plt.subplot(422)
plt.plot(upwindmethod(0.01,0.01,0)[0], 'o-',markersize=2.5)
plt.plot(upwindmethod(0.01,0.01,0)[1], '--')
plt.subplot(423)
plt.plot(upwindmethod(0.02,0.02,0.1)[0], 'o-',markersize=2.5)
plt.plot(upwindmethod(0.02,0.02,0.1)[1], '--')
plt.subplot(424)
plt.plot(upwindmethod(0.01,0.01,0.1)[0], 'o-',markersize=2.5)
plt.plot(upwindmethod(0.01,0.01,0.1)[1], '--')
plt.subplot(4, 2, 5)
plt.plot(upwindmethod(0.02,0.02,0.5)[0], 'o-',markersize=2.5)
plt.plot(upwindmethod(0.02,0.02,0.5)[1], '--')
plt.subplot(426)
plt.plot(upwindmethod(0.01,0.01,0.5)[0], 'o--',markersize=2.5)
plt.plot(upwindmethod(0.01,0.01,0.5)[1], '--')
plt.subplot(428)
plt.plot(upwindmethod(0.01,0.01,1)[0], 'o-',markersize=2.5)
plt.plot(upwindmethod(0.01,0.01,1)[1], '--')
plt.subplot(427)
plt.plot(upwindmethod(0.02,0.02,1)[0], 'o-',markersize=2.5)
plt.plot(upwindmethod(0.02,0.02,1)[1], '--')
plt.show()



