# -*- coding: utf-8 -*-

from scipy.stats import skew

dataList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( 'Simetrica: {}'.format( skew(dataList) ))


dataList = [1,1,2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( 'Asimetrica postivia: {}'.format( skew(dataList) ))

dataList = [1, 2, 3, 4, 5, 6, 7, 8, 8,9, 9,9,10]
print( 'Simetrica negativa: {}'.format( skew(dataList) ))

dataTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print( 'Simetrica: {}'.format( skew(dataTuple) ))


import pandas as pd
dataFrame = pd.DataFrame(dataList, columns =['valores'])
print(type(dataFrame))
print("Media del dataFrame usando Statistics es : % s " % (skew(dataFrame['valores'])))