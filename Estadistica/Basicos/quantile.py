# -*- coding: utf-8 -*-

import numpy as np
dataList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("lista : ", dataList) 
print("Q2 quantile para lista : ", np.quantile(dataList, .50))
print("Q1 quantile para lista : ", np.quantile(dataList, .25))
print("Q3 quantile para lista : ", np.quantile(dataList, .75))
print("100th quantile para lista : ", np.quantile(dataList, 0.1)) 