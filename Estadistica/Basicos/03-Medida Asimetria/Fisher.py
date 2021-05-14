# -*- coding: utf-8 -*-

from scipy.stats import skew

dataList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( 'Simetrica: {}'.format( skew(dataList) ))


dataList = [1,1,2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( 'Asimetrica postivia: {}'.format( skew(dataList) ))

dataList = [1, 2, 3, 4, 5, 6, 7, 8, 8,9, 9,9,10]
print( 'Simetrica negativa: {}'.format( skew(dataList) ))