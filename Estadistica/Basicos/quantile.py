# -*- coding: utf-8 -*-

import numpy as np
import statistics as st
dataList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("lista : ", st.median(dataList)) 
print("Q2 quantile para lista : ", np.quantile(dataList, .50))
print("Q1 quantile para lista : ", np.quantile(dataList, .25))
print("Q3 quantile para lista : ", np.quantile(dataList, .75))
print("100th quantile para lista : ", np.quantile(dataList, 1)) 

dataTuple = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("tupla : ", st.median(dataTuple)) 
print("Q2 quantile para tupla : ", np.quantile(dataTuple, .50))
print("Q1 quantile para tupla : ", np.quantile(dataTuple, .25))
print("Q3 quantile para tupla : ", np.quantile(dataTuple, .75))
print("100th quantile para tupla : ", np.quantile(dataTuple, 1)) 

import pandas as pd
dataFrame = pd.DataFrame(dataList, columns =['valores'])
print("Q2 quantile para dataFrame : ", np.quantile(dataFrame['valores'], .50))
print("Q1 quantile para dataFrame : ", np.quantile(dataFrame['valores'], .25))
print("Q3 quantile para dataFrame : ", np.quantile(dataFrame['valores'], .75))
print("100th quantile para dataFrame : ", np.quantile(dataFrame['valores'], 1)) 