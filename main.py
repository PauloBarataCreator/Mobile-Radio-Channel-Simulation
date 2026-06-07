import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

from numpy import random

ak = [1,1,0,1,0]
t  = np.arange(0,1,0.01)

t_variable = np.arange(0,len(ak),0.01)

fc = 1
sp = np.cos(2*np.pi*fc*t)
# estará retornando em uma faixa de 0 até 100, sendo 100 = 1s. Cada bloco de 100 em 100 é um símbolo.

abb = np.array([])
sm = np.array([])

sm_awgn = np.array([])


noise = np.random.normal(0,0.1,100)


rayleight_desv = random.rayleigh(size=100)
# y3 = np.convolve(z, x_volts) 

for k in ak:
    if k == 1:
        ele=1
    else:
        ele=-1
    
    # abb = np.append(abb, ele)
    abb = np.append(abb, ele*np.ones(len(t)))
    # np.ones gera um monte de números 1
    sm = np.append(sm, ele*sp)
    sm_awgn = np.append(sm_awgn, ele*sp*rayleight_desv + noise)
    # sm_awgn = np.append(sm_awgn, np.convolve(ele*sp, float(rayleight_desv)))

fig, ax = plt.subplots(2)
# ax[0].plot(t_variable,abb)
ax[0].plot(t_variable,sm)
ax[1].plot(t_variable,sm_awgn)

# plt.plot(abb)
plt.show()


print(abb)
# print(sm)
# print(t)