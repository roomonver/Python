# -*- coding: utf-8 -*-

from scipy import stats as stats
'''
Distribucion binomial acumulada

parametro 1 es el número de éxitos en las pruebas, un valor numérico mayor o igual a 0.
parametro 2 es el número de pruebas, un valor numérico mayor o igual a número-s.
parametro 3 es la probabilidad de éxito de cada prueba, un valor numérico mayor o igual a 0 pero menor o igual a 1.
'''
acumulada = stats.binom.cdf(25,30, 0.8)
print(acumulada)

puntual = stats.binom.pmf(k=25,n=30,p=0.8)
print(puntual)
