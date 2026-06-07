import numpy as np

import matplotlib.pyplot as plt

import math

ak = [1,0,0,1]
ak2 = [0,0,0,0]


t  = np.arange(0,1,0.01)

t_variable = np.arange(0,len(ak),0.01)

fc = 1
sp = np.cos(2*np.pi*fc*t)
sp_ = np.cos(2*np.pi*fc*t + np.pi)

sp2 = np.cos(2*np.pi*fc*t+ 3.0*np.pi)
sp2_ = np.cos(2*np.pi*fc*t)
#  + np.pi



abb = np.array([])
sm = np.array([])

sm2 = np.array([])

for k in ak:
    if k == 1:
        # ele=1
        ele = sp

        ele2 = sp2
    else:
        # ele=-1
        ele = sp_

        ele2 = sp2_
    
    abb = np.append(abb, ele*np.ones(len(t)))
    sm = np.append(sm, ele)
    sm2 = np.append(sm2, ele + ele2)

fig, ax = plt.subplots(2)
# ax[0].plot(t_variable,abb)
ax[0].plot(t_variable,sm)
ax[1].plot(t_variable,sm2)
# ax[0].plot(sp)
# ax[1].plot(sp_)
plt.show()













# plt.plot(abb)
# print(abb)
