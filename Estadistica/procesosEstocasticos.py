# -*- coding: utf-8 -*-


import numpy as np
from scipy import stats as stats
import matplotlib.pyplot as plt

def camino_aleatorio(n, probs, X0 = 0):
    pac = np.cumsum(probs)
    a = stats.uniform.rvs(size=n)
    Z = np.where(a < pac[0], -1, np.where(a < pac[1], 0, 1))
    aux = X0 + np.cumsum(Z)
    return aux
  
ca=camino_aleatorio(n = 10, probs =[0.2, 0.5, 0.3])

plt.plot(ca,'.-');
plt.title('Recorrido Aleatorio');
plt.ylabel("Posición");
plt.xlabel("Etapa")
plt.show()

#Paseo más largo:
ca=camino_aleatorio(n = 50, probs =[0.2, 0.5, 0.3])
plt.plot(ca,'.-');
plt.title('Recorrido Aleatorio');
plt.ylabel("Posición");
plt.xlabel("Etapa")
plt.show()

#Y varios paseos:
ca=camino_aleatorio(n = 50, probs =[0.2, 0.5, 0.3])

plt.plot(ca,'.-',zorder=-1);
plt.title('Recorrido Aleatorio')
plt.ylabel("Posición");
plt.xlabel("Etapa");

for i in np.arange(0,10):
    ca=camino_aleatorio(n = 50, probs =[0.2, 0.5, 0.3])
    plt.plot(ca,'.-',zorder=i)