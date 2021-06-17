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
def lecturaFila():
    
    cuerpo = driver.find_element_by_xpath('//div[@id="resultado"]')   
    filas = cuerpo.find_elements_by_xpath('//tbody/tr[@ng-repeat="row in $data"]')
    for fila in filas:
        
        # print("*" * 30)
        objetoFila = fila.find_element_by_xpath('.//td[@class="ng-binding"]')
        print(objetoFila.text )
        objetoFilaText = fila.find_element_by_xpath('.//td[text()= "' + objetoFila.text + '"]')
        # print(objetoFilaText.text)
        action.move_to_element(objetoFilaText).perform()
        sleep(0.1)
        
        
        tabla = driver.find_element_by_xpath('//table[@class="datos-vehiculo"]')
        # print("*"*30)
        # print(tabla.get_attribute('innerHTML'))
        

driver = webdriver.Chrome('./chromedriver.exe')

#para acceder a una url
url = 'http://www.consumovehicular.cl/comparador#/'
driver.get(url)

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
pTermino = 2
tPaginadorWait = 0.3
i=0


    
while( i < int(pTermino) ):
    
    try:
        
         action = ActionChains(driver)
         print("pagina: ", (i+1))
         lecturaFila()
         i = avanzaPaginacion(i,pTermino)
         
         
    except Exception as e:
        print(e)
        sleep(tPaginadorWait)
       
   