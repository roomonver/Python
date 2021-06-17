# -*- coding: utf-8 -*-


import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


'''
Avanzar paginacion
'''
def avanzaPaginacion(i,pTermino):
    
    pActiva = listaUl.find_element_by_xpath('.//li[@class="page-item ng-scope active"]').text
    print(pActiva, pTermino)
    avanzar = listaUl.find_element_by_xpath('.//a[@ng-switch-when="next"]')
    if (int(pActiva) <= int(pTermino)):
       avanzar.click()
       sleep(tPaginadorWait)
       i=i+1
       action.move_to_element(buscarAutos).perform()
    return i

'''
Lectura de Tabla
'''
def lecturaFila():
    
    cuerpo = buscarAutos.find_element_by_xpath('//div[@id="resultado"]')   
    filas = cuerpo.find_elements_by_xpath('//tbody/tr[@ng-repeat="row in $data"]')
    for fila in filas:
        
        # print("*" * 30)
        print(fila.find_element_by_xpath('.//td[@class="ng-binding"]').text )
        
        

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


action = ActionChains(driver)
'''
Lectura y control de paginador
'''
listaUl = driver.find_element_by_xpath('//ul[@ng-if="pages.length"]')
pActiva = listaUl.find_element_by_xpath('.//li[@class="page-item ng-scope active"]').text
pTermino = listaUl.find_element_by_xpath('.//a[@ng-switch-when="last"]').text
pTermino = 1
tPaginadorWait = 0.3
i=1


    
while( i <= int(pTermino) ):
    
    try:
        
         i = avanzaPaginacion(i,pTermino)
         lecturaFila()
         
    except Exception as e:
        print(e)
        sleep(tPaginadorWait)
       
   