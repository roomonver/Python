# -*- coding: utf-8 -*-

from scipy import stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

muestra_binomial = stats.binom.rvs(n=10,p=0.4,size=100)
pd.Series(muestra_binomial).value_counts().sort_index().plot(kind='bar');
plt.show()

print("(a). P(X=4)")
teorica = stats.binom.pmf(k=4,n=10,p=0.4)
print("Teorica: ", teorica)

print("P(X≤4)")
teorica = stats.binom.cdf(k=4,n=10,p=0.4)
print("Teorica: ", teorica)

print("k:P(X≤k)=0.68")
teorica = stats.binom.ppf(q=0.68,n=10,p=0.4)
empirica = np.quantile(muestra_binomial,0.68)
print("Teorica: ", teorica)
print("Empirica: ", empirica)


eje_x = np.arange(0,10)
eje_y = stats.binom.pmf(k=eje_x,n=10,p=0.4)
pd.Series(muestra_binomial).value_counts('%').sort_index().plot(kind='bar',zorder=-1);
plt.scatter(eje_x, eje_y,color='red',zorder=1);
plt.show()