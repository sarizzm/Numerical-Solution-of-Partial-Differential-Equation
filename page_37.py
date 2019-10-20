import  numpy as np
import matplotlib.pyplot as plt
from scipy import linalg
from scipy import integrate
from theta_new import theta_method


def am(m):
   def f(x):
      return x * (1 - x) * np.sin(m * np.pi * x)

   v, err = integrate.quad(f, 0, 1)
   return 2 * v


Am = [am(i) for i in range(100)]


# print(Am.__len__())
def ur(x, t):
   u = 0
   for i in range(100):
      u = u + Am[i] * np.exp(-(i * np.pi) ** 2 * t) * np.sin(i * np.pi * x)
   return u


def three_m(nu, mu1, mu2, mu3):
   u_1_t = np.zeros((nu, nu + 2))
   for i in np.arange(1, nu + 1, 1):
      u_1_t[i - 1, i] = mu2  # 1 + 2 * mu1
      u_1_t[i - 1, i + 1] = mu3
      u_1_t[i - 1, i - 1] = mu1
   return u_1_t[:, 1:nu + 1]


def theta_method(theta, J, miu, v):
   delta_x = 1 / J
   if v == 0:
      delta_t = miu * delta_x ** 2
   else:
      delta_t = v * delta_x
      miu = delta_t / delta_x ** 2
   x = np.linspace(0, 1, J + 1)
   # print(x)
   implicmatrix = three_m(J - 1, -theta * miu, (1 + 2 * theta * miu), (-theta * miu))
   explicmatrix = three_m(J - 1, (1 - theta) * miu, (2 * theta * miu - 2 * miu + 1), (1 - theta) * miu)
   U0 = x * (1 - x)
   u2 = U0
   # print(U0)
   U0 = U0[1:J]
   print('uo2',U0)
   # print(implicmatrix)
   # print(explicmatrix)
   u = np.copy(U0)
   error = []
   if theta != 0:
      for k in range(int(np.floor(1 / delta_t))):
         # %every time we use the previous matrix generating all Un
         U0 = linalg.solve(np.array(implicmatrix),np.array(explicmatrix)*np.mat(U0).T)
         U0=U0.flatten()
         if k * delta_t >= 0.1:
            for i in range(J - 1):
               u[i] = ur(x[i + 1], k * delta_t)
            # asd =U0 - u
            error.append(np.abs(U0 - u))

            # print(np.abs(U0))
            # print(error.shape)
            # print(u)
            # print(U0)
            # print(u-U0)

   else:
      for k in range(1, int(np.floor(1 / delta_t))):
         U0 = np.array(explicmatrix) * np.mat(U0).T
         U0 = U0.flatten()
         U0 = U0.flatten().A[0]
         if k * delta_t >= 0.1:
            for i in range(J - 1):
               u[i] = ur(x[i + 1], k * delta_t)
            error.append(np.abs(U0 - u))

   return error



J=20

# %A:theta=0,miu=1/2

error1 = np.array(theta_method(1,20,1,0))
# plt.semilogx(J,error1,'-ok')

error2 = np.array(theta_method(0,20,2,0))
print(error1.shape)
print(error2.shape)
# print(error2[1])

plt.subplot(421)
plt.plot(error1[0], 'ro-')
plt.subplot(422)
plt.plot(error2[0], 'o-')
plt.subplot(423)
plt.plot(error1[1], 'o-')
plt.subplot(424)
plt.plot(error2[1], 'o-')
plt.subplot(4, 2, 5)
plt.plot(error1[2], 'o-')
plt.subplot(426)
plt.plot(error2[2], 'o-')
plt.subplot(427)
plt.plot(error1[10], 'o-')
plt.subplot(428)
plt.plot(error2[10], 'o-')
plt.show()