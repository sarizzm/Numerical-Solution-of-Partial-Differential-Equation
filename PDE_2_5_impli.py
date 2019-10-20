import  numpy as np
import matplotlib.pyplot as plt
from scipy import linalg


def main():


    delt1 = 0.0013
    delt2 = 0.0012
    delx = 0.05
    mu1 = delt1 / (delx ** 2)
    mu2 = delt2 / (delx ** 2)
    # mu = 0.52
    u = np.zeros((int(1 / delx) + 1, 51))
    U = np.zeros((int(1 / delx) + 1, 51))
    u_1_t = np.zeros((int(1 / delx) -1, int(1 / delx) -1))
    u_2_t = np.zeros((int(1 / delx) - 1,int(1 / delx) -1))

    for i in range(21):

        x = delx * (i)
        if x <= 0.5:
            u[i, 0] = 2 * x
            U[i, 0] = 2 * x
        else:
            u[i, 0] = 2 - 2 * x
            U[i, 0] = 2 - 2 * x


    print(u.shape)

    for i in np.arange(1, int(1 / delx) - 2, 1):
        u_1_t[i, i] = 1 + 2 * mu1
        u_1_t[i, i + 1] = -mu1
        u_1_t[i, i - 1] = -mu1
    print(u_1_t.shape)
    u_1_t[0,0] = 1 + 2 * mu1
    u_1_t[0, 1] = - mu1
    u_1_t[18, 17] = - mu1
    u_1_t[18, 18] = 1 + 2 * mu1
    # print(u_1_t)
    print(u)
    k = 1
    for j in np.arange(0,50,1):
        # for k in np.arange(1,20,1):

        u[1:20,j+1] = linalg.solve(u_1_t,u[1:20,j])
        U[1:20, j + 1] = linalg.solve(u_1_t, U[1:20, j])


    # 绘图
    plt.subplot(421)
    plt.plot(np.linspace(0, 1, int(1 / delx) + 1), U[:, 0],'o-')
    plt.subplot(422)
    plt.plot(np.linspace(0, 1, int(1 / delx) + 1), u[:, 0],'o-')
    plt.subplot(423)
    plt.plot(np.linspace(0, 1, int(1 / delx) + 1), U[:, 1],'o-')
    plt.subplot(424)
    plt.plot(np.linspace(0, 1, int(1 / delx) + 1), u[:, 1],'+-')
    plt.subplot(4, 2, 5)
    plt.plot(np.linspace(0, 1, int(1 / delx) + 1), U[:, 24],'o-')
    plt.subplot(426)
    plt.plot(np.linspace(0, 1, int(1 / delx) + 1), u[:, 24],'o-')
    plt.subplot(427)
    plt.plot(np.linspace(0, 1, int(1 / delx) + 1), U[:, 49],'o-')
    plt.subplot(428)
    plt.plot(np.linspace(0, 1, int(1 / delx) + 1), u[:, 49],'o-')
    plt.show()


if __name__ =='__main__':
    main()
