# -*- coding: utf-8 -*-


import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


'''
Avanzar paginacion
'''
def avanzaPaginacion(i,pTermino):
    
    buscarAutos = driver.find_element_by_xpath('//button[@class="form-submit ajax-processed"]')
    action.move_to_element(buscarAutos).perform()
    pActiva = listaUl.find_element_by_xpath('.//li[@class="page-item ng-scope active"]').text
    print("Activa: ", pActiva, ", Termino: ", pTermino)
    avanzar = driver.find_element_by_xpath('.//a[@ng-switch-when="next"]')
    if (int(pActiva) <= int(pTermino)):
       avanzar.click()
       sleep(tPaginadorWait)
       i=i+1
    return i

'''
Lectura de Tabla
'''
def lecturaFila(listaAuto):
    
    cuerpo = driver.find_element_by_xpath('//div[@id="resultado"]')   
    filas = cuerpo.find_elements_by_xpath('//tbody/tr[@ng-repeat="row in $data"]')
   
    for fila in filas:
        
        # print("*" * 30)
        objetoFila = fila.find_element_by_xpath('.//td[@class="ng-binding"]')
        print(objetoFila.text )
        try:
            objetoFilaText = fila.find_element_by_xpath('.//td[text()= "' + objetoFila.text + '"]')
        except Exception as e:    
            objetoFilaText = ""
            print("**No se encontro registro para elemento ", objetoFila.text)
            print(e)
        
        if (objetoFilaText!=""):
            action.move_to_element(objetoFilaText).perform()
            sleep(0.2)
            
            '''
            lectura caracteristicas del auto
            '''
            tabla = driver.find_element_by_xpath('//table[@class="datos-vehiculo"]')
            auto = lecturaDetalle(tabla)
            listaAuto.append(auto)
    
    return(listaAuto)
        

def lecturaDetalle(tabla):
    # print(tabla.get_attribute('innerHTML'))
    
    elementoModelo = tabla.find_element_by_xpath('.//thead/tr/td')
    modelo = elementoModelo.get_attribute('innerHTML')
    modelo = modelo.replace('<span class="titulo-azul">Modelo:</span>',"").strip()
    print("**Modelo[{0}]".format(modelo))
    
    filas = tabla.find_elements_by_xpath('.//tbody/tr')
    i = 1
    
    
    for fila in filas:
        
        # codigoInformeTecnico = fila.find_elements_by_xpath('.//td')[0].get_attribute('innerHTML')
        # marca = fila.find_elements_by_xpath('.//td')[1].get_attribute('innerHTML')
        if (i==1):
            codigoInformeTecnico = fila.find_elements_by_xpath('.//td')[0].get_attribute('innerHTML')
            marca = fila.find_elements_by_xpath('.//td')[1].get_attribute('innerHTML')
            # print(codigoInformeTecnico, marca)
        elif (i==2):
            traccion = fila.find_elements_by_xpath('.//td')[0].get_attribute('innerHTML')
            propulsion = fila.find_elements_by_xpath('.//td')[1].get_attribute('innerHTML')
            # print(traccion, propulsion)
        elif (i==3):
            transmision = fila.find_elements_by_xpath('.//td')[0].get_attribute('innerHTML')
            carroceria = fila.find_elements_by_xpath('.//td')[1].get_attribute('innerHTML')
            # print(transmision, carroceria)
        elif (i==4):
            cilindrada = fila.find_elements_by_xpath('.//td')[0].get_attribute('innerHTML')
            fCertificacion = fila.find_elements_by_xpath('.//td')[1].get_attribute('innerHTML')
            # print(cilindrada, fCertificacion)
        elif (i==5):
            categoria = fila.find_elements_by_xpath('.//td')[0].get_attribute('innerHTML')
            norma = fila.find_elements_by_xpath('.//td')[1].get_attribute('innerHTML')
            # print(categoria, norma)
        elif (i==6):
            co2 = fila.find_elements_by_xpath('.//td')[0].get_attribute('innerHTML')
            rCiudad = fila.find_elements_by_xpath('.//td')[1].get_attribute('innerHTML')
            # print(co2, rCiudad)
        elif (i==7):
            rCarretera = fila.find_elements_by_xpath('.//td')[0].get_attribute('innerHTML')
            rMixto = fila.find_elements_by_xpath('.//td')[1].get_attribute('innerHTML')
            # print(rCarretera, rMixto)
        i = i+1
    
    auto = dict(modelo = modelo,
                codigoInformeTecnico = codigoInformeTecnico,
                marca = marca,
                traccion = traccion,
                propulsion = propulsion,
                transmision = transmision,
                carroceria = carroceria,
                cilindrada = cilindrada,
                fCertificacion = fCertificacion,
                categoria = categoria,
                norma = norma,
                co2 = co2,
                rCiudad = rCiudad,
                rCarretera = rCarretera,
                rMixto = rMixto
                )
    return(auto)
    
    
    
  

driver = webdriver.Chrome('./chromedriver.exe')

#para acceder a una url
url = 'http://www.consumovehicular.cl/comparador#/'
driver.get(url)
sleep(5)
'''
buscar los autos
'''
buscarAutos = driver.find_element_by_xpath('//button[@class="form-submit ajax-processed"]')
buscarAutos.click()
sleep(0.5)

'''
Lectura y control de paginador
'''
listaUl = driver.find_element_by_xpath('//ul[@ng-if="pages.length"]')
pActiva = listaUl.find_element_by_xpath('.//li[@class="page-item ng-scope active"]').text
pTermino = listaUl.find_element_by_xpath('.//a[@ng-switch-when="last"]').text
# pTermino = 1
tPaginadorWait = 0.6
i=0


listaAuto = list()
while( i < int(pTermino) ):
    
    try:
        
         action = ActionChains(driver)
         print("pagina: ", (i+1))
         listaAuto = lecturaFila(listaAuto)
         i = avanzaPaginacion(i,pTermino)
         
         
    except Exception as e:
        print(e)
        i=i+1
        sleep(1)

import pandas as pd
df = pd.DataFrame(listaAuto)
df.to_excel("consumoVehicular.xlsx")
df.to_csv("consumoVehicular.csv")