# -*- coding: utf-8 -*-

import pandas as pd
import scipy.stats as stats 
import matplotlib.pyplot as plt
import numpy as np
salud = pd.read_csv("ESalud19.csv")

'''
(a) La probabilidad que una persona fume actualmente uno o más cigarros está dada por:
'''
a = len(salud[salud["FUMA_ACTUAL"]=='SÍ, UNO O MÁS CIGARRILLOS AL DÍA']) / len(salud["FUMA_ACTUAL"])
print("Respuesta A: ", a )

'''
(b)  La probabilidad que una persona fume actualmente Y que no tenga diabetes:
'''
b = len(salud[(salud["FUMA_ACTUAL"]=='SÍ, UNO O MÁS CIGARRILLOS AL DÍA') & (salud["DIABETES"]=="NO") ]) / len(salud["FUMA_ACTUAL"])
print("Respuesta B: ", b )


'''
(c) La probabilidad que una persona, que fume actualmente, no tenga diabetes:
'''

noDiabete = salud.loc[ salud["DIABETES"] == "NO", ["FUMA_ACTUAL"] ]
cNoDiabeteFuma = len(noDiabete[noDiabete["FUMA_ACTUAL"]=='SÍ, UNO O MÁS CIGARRILLOS AL DÍA'])
cTotalFuma = len(salud[salud["FUMA_ACTUAL"]=='SÍ, UNO O MÁS CIGARRILLOS AL DÍA'])

print("Respuesta C: ", (cNoDiabeteFuma / cTotalFuma))


'''
(d) La probabilidad que una persona que no tenga diabetes, fume actualmente es:
'''
noFuma = salud.loc[ salud["FUMA_ACTUAL"] == "SÍ, UNO O MÁS CIGARRILLOS AL DÍA", ["DIABETES"] ]
cNoDiabeteFuma = len(noFuma[noFuma["DIABETES"]=='NO'])
cDiabete = len(salud[salud["DIABETES"]=='NO'])

print("Respuesta D: ", (cNoDiabeteFuma / cDiabete))



'''
Actividad
Utilizando los datos de Salud, responda:
'''

#1-.¿Cuál es la probabilidad de seleccionar una persona que haga DEPORTE?
a = len(salud[salud["DEPORTE"]=='SÍ']) / len(salud["DEPORTE"])
print("Respuesta A: ", a )

#2-.¿Cuál es la probabilidad de seleccionar una persona que esté SOLTERO(A)?
b =len(salud[salud["E_CIVIL"]=='SOLTERO(A)']) /  len(salud["E_CIVIL"])
print("Respuesta B: ",b)

#3-.¿Cuál es la probabilidad que una persona, que hace deporte, esté SOLTERO(A)?
haceDeporte = salud.loc[salud["DEPORTE"]=='SÍ',["E_CIVIL"]]
cSolteroHaceDeporte = sum(haceDeporte["E_CIVIL"]=='SOLTERO(A)')
cSoltero = sum(salud["DEPORTE"]=='SÍ')
print("Respuesta C: ",(cSolteroHaceDeporte/cSoltero))

#4-.Dado que la persona no está SOLTERO(A), ¿Cuál es la probabilidad que no haga deporte?
noSolteros =  salud.loc[salud["E_CIVIL"]!='SOLTERO(A)',["DEPORTE"]]
cNoDeporte = sum(noSolteros["DEPORTE"]=="NO")
cNoSolteros = sum(salud["E_CIVIL"]!='SOLTERO(A)')
print("Respuesta D: ", (cNoDeporte/ cNoSolteros))







