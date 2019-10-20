import  numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

 # Fourier analysis
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

def main():

    # 初始值
    delx_1 = 0.1
    delx_2 = 0.05
    mu = 0.5
    delt_1 = mu * (delx_1**2)
    delt_2 = mu * (delx_2**2)

    # 初始化 u1 , u2
    u_1 = np.zeros((11,200))
    u_2 = np.zeros((21,800))
    i = 0 # u1初始化
    u1_real = np.copy(u_1)
    u2_real = np.copy(u_2)
    for u1 in u_1:
        u1[0] = i*delx_1*(1-i*delx_1)
        i = i+1
    i = 0  # u2初始化
    for u2 in u_2:
        u2[0] = i*delx_2*(1-i*delx_2)
        i =i+1
    print(u_1.shape)
    # 获取x 的 离散坐标
    u_1_co = np.linspace(0, 1, int(1 / delx_1) + 1)
    u_2_co =np.linspace(0, 1, int(1 / delx_2) + 1)

    # 构造 u1 ,u2 的迭代矩阵
    u_1_t = np.zeros((11,11))
    u_2_t = np.zeros((21,21))
    print(u_1_t.shape)
    # print(np.arange(1,11,1))   #arange [ 1  2  3  4  5  6  7  8  9 10]
    for i in np.arange(1,10,1):
        u_1_t[i,i] = 1-2*mu
        u_1_t[i , i+1] = mu
        u_1_t[i, i-1] = mu
    print(u_1_t)
    for i in np.arange(1,20,1):
        u_2_t[i,i] = 1-2*mu
        u_2_t[i , i+1] = mu
        u_2_t[i, i-1] = mu


    #计算u_1
    for j in np.arange(0,198,1):
        u_1[:,j+1] =np.dot( u_1_t ,u_1[:,j])
    #计算u_2
    for j in np.arange(0,798,1):
        u_2[:,j+1] =np.dot( u_2_t ,u_2[:,j])


    # 傅里叶 求 相应的近似真实值
    # print(u_1[:, 20])
    for j in range(len(u_1[:,1])):

        for  i in range(len(u_1[1,:])):
            u1_real[j,i]= ur(u_1_co[j], i*delt_1)
            # print(u)
    for j in range(len(u_2[:,1])):

        for  i in range(len(u_2[1,:])):
            u2_real[j,i]= ur(u_2_co[j], i*delt_2)

    # 计算每个时间步的误差的最大值
    p_u_1 = u_1-u1_real
    p_u_2 = u_2 - u2_real
    u1_y = [np.log10(np.max(np.abs(p_u_1[:, i])))  for  i in range(len(p_u_1[1,:])-1)]
    u2_y = [np.log10(np.max(np.abs(p_u_2[:, i]))) for i in range(len(p_u_2[1, :]) - 1)]

    # 绘图
    plt.xlim((0, 1.05))
    plt.plot(np.linspace(0,1,len(u1_y[0:-2])),u1_y[0:-2])
    plt.plot(np.linspace(0, 1, len(u2_y[0:-2])), u2_y[0:-2])
    plt.show()
    # print(u_2[:,-1])



if __name__ =='__main__':
    main()
