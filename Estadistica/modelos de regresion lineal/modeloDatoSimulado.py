# -*- coding: utf-8 -*-
'''
Modelo con datos simulados

y = a + b * x
x : 100 valores distribuisos segun una N (1,5, 2.5)
Ye = 2 + 1.9 * x + e
e estara distribuida segun una N(0, 0.8)


'''

import pandas as pd
import numpy as np
x = 1.5 + 2.5 * np.random.randn(100)
res = 0 + 0.8 * np.random.randn(100)
y_pred = 5 + 1.9 * x
y_act = 5 + 1.9 * x + res


#transformar array en listas para posterioirmetne hacerlo un df
x_list = x.tolist()
y_pred_list = y_pred.tolist()
y_act_list = y_act.tolist()

data = pd.DataFrame(
                        {
                        'x':x_list,
                        'y_pred':y_pred_list,
                        'y_act': y_act_list
                        }
                    )

y_mean = [np.mean(y_act) for i in range(1, len(x_list)+1)]

import matplotlib.pyplot as plt

plt.plot(x, y_pred)
plt.plot(x, y_act, 'ro')
plt.plot(x, y_mean)
plt.title("Valor Actual vs Prediccion")
plt.show()

data['SSR'] = (data['y_pred']- np.mean(y_act))**2
data['SSD'] = (data['y_pred'] - data['y_act'])**2
data['SST'] = (data['y_act']-np.mean(y_act))**2

SSR = sum(data['SSR'])
SSD = sum(data['SSD'])
SST = sum(data['SST'])
print(SSR , SSD, SST)

R2 = SSR/SST
print("R2 1:", R2)

plt.hist((data['SSD'] - data['y_act']))
plt.show()


'''
Obtener recta de regresion

y = a + b * x
b = sum( (xi - x_m)*(yi - y_m) )/ sum((xi - x_m)**2)
a = y_m - b * x_m
'''
x_mean = np.mean(data['x'])
y_mean = np.mean(data['y_act'])


data['beta_n'] = (data['x'] - np.mean(data['x'])) * (data['y_act'] - np.mean(data['y_act']))
data['beta_d'] = (data['x'] - x_mean)**2
beta = sum(data['beta_n'])/sum(data['beta_d'])
alpha = y_mean - beta * x_mean

#print(alpha, beta)
data['y_model'] = alpha + beta * data['x']


'''
Modelo lineal obtenido por regresion
y = a+b*x
'''
SSR = sum((data['y_model']-y_mean)**2)
SSD = sum((data['y_model']-data['y_act'])**2)
SST = sum((data['y_act']-y_mean)**2)
print(SSR , SSD, SST)

R2 = SSR/SST
print("R2 2:", R2)

y_mean = [np.mean(y_act) for i in range(1, len(x_list)+1)]
plt.plot(x, y_pred)
plt.plot(x, y_act, 'ro')
plt.plot(x, y_mean, "g")
plt.plot(data['x'], data['y_model'])
plt.title("Valor Actual vs Prediccion")
plt.show()