import  numpy as np
import matplotlib.pyplot as plt
from scipy import linalg
from scipy import integrate
def am(m):
    def f(x):
        return x*(1-x)*np.sin(m*np.pi*x)
    v, err = integrate.quad(f, 0, 1)
    return 2*v
Am  =  [am(i) for i in range(30)]
# print(Am.__len__())
def ur(x,t):
    u = 0
    for i in range(30):
        u = u + Am[i] * np.exp(-(i*np.pi)**2*t)*np.sin(i*np.pi*x)
    return u

def three_m(nu,mu1,mu2,mu3):
    u_1_t = np.zeros((nu, nu+2))
    for i in np.arange(1, nu+1 , 1):
        u_1_t[i-1, i] = mu2#1 + 2 * mu1
        u_1_t[i-1, i + 1] = mu3
        u_1_t[i-1, i - 1] = mu1
    return u_1_t[:,1:nu+1]


def theta_method(theta,J,miu,v):
    delta_x=1/J
    if v==0 :
        delta_t=miu*delta_x**2
    else:
        delta_t=v*delta_x
        miu=delta_t/delta_x**2
    x=np.linspace(0,1,J+1)
    # print(x)
    implicmatrix= three_m(J-1,-theta*miu,(1+2*theta*miu),(-theta*miu))
    explicmatrix=three_m(J-1,(1-theta)*miu,(2*theta*miu-2*miu+1),(1-theta)*miu)
    U0=x*(1-x)
    # print(U0)
    U0=U0[1:J]
    # print('uo2',U0)
    # print(implicmatrix)
    # print(explicmatrix)
    u=np.copy(U0)
    error=[]
    if theta != 0 :
        for k in range(1,int(np.floor(1/delta_t))):
        # %every time we use the previous matrix generating all Un
        #     U0=linalg.solve(implicmatrix,explicmatrix*U0)
            U0 = linalg.solve(np.array(implicmatrix), np.array(explicmatrix) * np.mat(U0).T)
            U0 = U0.flatten()
            if k*delta_t>=0.1:
                for i in range(J-1) :
                    u[i]= ur(x[i+1],k*delta_t)
                error.append( np.max(np.abs(U0-u)))
                # print(u)
                # print(U0)
                # print(u-U0)

    else:
        for k in range(1,int(np.floor(1/delta_t))):
            U1=np.array(explicmatrix) * np.mat(U0).T
            U0=U1.flatten().A[0]
            if k*delta_t >= 0.1:
                for i in range(J-1):
                    u[i]=ur(x[i+1],k*delta_t)
                error.append( np.max(np.abs(U0-u)))

    return np.max(error)

