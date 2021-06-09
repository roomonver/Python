# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('advertising.csv')

import statsmodels.formula.api as smf

lm = smf.ols(formula = "Sales~TV")
