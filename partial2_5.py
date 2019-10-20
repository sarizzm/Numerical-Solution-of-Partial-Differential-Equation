import  numpy as np
import matplotlib.pyplot as plt

def main():
    delt1 = 0.0013
    delt2 = 0.0012
    delx = 0.05
    mu1 = delt1/(delx**2)
    mu2 = delt2/(delx**2)
    # mu = 0.52
    u = np.zeros((int(1/delx)+1,51))
    U =np.zeros((int(1/delx)+1,51))


    for i in range(21):

        x= delx *(i)
        if x<= 0.5:
            u[i,0]=2*x
            U[i,0]=2*x
        else:
            u[i,0] = 2-2 * x
            U[i,0] = 2-2 * x
    for j in np.arange(0,50,1):
        for k in np.arange(1,20,1):

            u[k,j+1] = u[k,j] + mu1 * (u[k+1,j ] - 2 * u[k,j] + u[k-1,j ])
            U[k, j + 1] = U[k, j] + mu2 * (U[k + 1, j] - 2 * U[k, j] + U[k - 1, j])

    plt.subplot(421)
    plt.plot(np.linspace(0, 1, int(1 / delx) + 1), U[:, 0], 'o-')
    plt.subplot(422)
    plt.plot(np.linspace(0, 1, int(1 / delx) + 1), u[:, 0], 'o-')
    plt.subplot(423)
    plt.plot(np.linspace(0, 1, int(1 / delx) + 1), U[:, 1], 'o-')
    plt.subplot(424)
    plt.plot(np.linspace(0, 1, int(1 / delx) + 1), u[:, 1], 'o-')
    plt.subplot(4, 2, 5)
    plt.plot(np.linspace(0, 1, int(1 / delx) + 1), U[:, 24], 'o-')
    plt.subplot(426)
    plt.plot(np.linspace(0, 1, int(1 / delx) + 1), u[:, 24], 'o-')
    plt.subplot(427)
    plt.plot(np.linspace(0, 1, int(1 / delx) + 1), U[:, 49], 'o-')
    plt.subplot(428)
    plt.plot(np.linspace(0, 1, int(1 / delx) + 1), u[:, 49], 'o-')
    plt.show()


if __name__ =='__main__':
    main()
