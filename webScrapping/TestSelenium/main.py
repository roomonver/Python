# -*- coding: utf-8 -*-

'''
Tutorial seguido
https://www.youtube.com/watch?v=fM_Os976HsQ

* * * * * S E L E N I U M * * *

1)Como primer paso se debe instalar la libreria de Selenium

pip install selenium.

2) se debe instalar el controlador segun navegador.
para este caso el google chrome desde el link
https://sites.google.com/a/chromium.org/chromedriver/downloads

tienes que ser la misma version de navegador y sistema operativo.
'''


import random
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')

#para acceder a una url
url = 'https://ww2.banchileinversiones.cl/web/personas/p-fondos-mutuos'
driver.get(url)

#Buscar las ventajas de los fondos mutuos
contenedorVentajas = driver.find_elements_by_class_name('contenedorVentajas')

'''
para buscar con xpath es importante especificar .// para que busco dentro del elemento actual
'''
#Sitio posee 2 secciones con class 'contenedorVentajas'
ventajas  = contenedorVentajas[0].find_elements_by_xpath('.//div/div')
for ventaja in ventajas:
    textos = ventaja.find_elements_by_xpath('.//p')
    titulo = textos[0].text
    detalle  = textos[1].text
    print(titulo, detalle)


'''
Buscar valores cuotas de todos los fondos mutuos
'''

#Hacer click en boton buscar
buscarFondos = driver.find_element_by_xpath('//button[@ng-click="buscarFondos(true);"]')
buscarFondos.click()

#find dropdown and click to open options 
input = driver.find_element_by_xpath("//md-select[@ng-model='itemCantidad']")
# a traves de este comando abro la lista
driver.execute_script('arguments[0].click();', input)
# espero 2 segundos para que la lista se alcance a dibujar y exista el elemento a buscar
sleep(2)
# Busco la opcion que quiero y hago clic en ella para listar todos los fondos mutuos.
opcion =  driver.find_element_by_xpath("//md-option[@id='select_option_16']")
opcion.click()

cuerpoTabla = driver.find_element_by_xpath('//tbody[@ng-show="renderBusquedaFMOk"]')
fondos = cuerpoTabla.find_elements_by_xpath('.//tr[@class="ng-scope"]')

nemoLista = list()
varDiaLista = list()
var30Lista = list()
varAñoList = list()
valorCuota = list()
i = 0
for fondo in fondos:
    
    # fondo.find_elements_by_xpath('//tbody[@data-title="Fondo Mutuo"]')
    nemoLista.append(fondo.find_element_by_xpath('.//td[@data-title="Fondo Mutuo"]').text )
    varDiaLista.append(fondo.find_element_by_xpath('.//td[@data-title="Var. % diaria"]').text)
    var30Lista.append(fondo.find_element_by_xpath('.//td[@data-title="Var. % 30 días"]').text)
    varAñoList.append(fondo.find_element_by_xpath('.//td[@data-title="Var. % Acu. año"]').text)
    valorCuota.append(fondo.find_element_by_xpath('.//td[@data-title="Valor Cuota"]').text)
    print(i)
    i+=1

import pandas as pd
dfFondosMutuos = pd.DataFrame(list(zip(nemoLista,
                                        varDiaLista,
                                        var30Lista,
                                        varAñoList,
                                        valorCuota)),
                              columns = ["Fondo Mutuos",
                                         "Variacion Diaria",
                                         "Variacion 30 dias",
                                         "Variacion Acumulada Año",
                                         "Valor Cuota"])

from datetime import date
today = date.today()

dfFondosMutuos.to_csv('FondosMutuos{0}.csv'.format(today))

