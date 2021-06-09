# -*- coding: utf-8 -*-

import pandas as pd

iris = pd.read_csv("https://raw.githubusercontent.com/toneloy/data/master/iris.csv")

print((iris.groupby("species")
           .agg(frequency=("species", "count"))))

#Graficar Tabla de frecuencias
from plotnine import ggplot, aes,geom_bar

freq_by_species = (iris.groupby("species")
                       .agg(frequency=("species", "count"))
                       .reset_index())
  
graficoFrecuencia = (ggplot(freq_by_species, aes(x = "species", y = "frequency")) +
  geom_bar(stat = 'identity'))
graficoFrecuencia.draw()



