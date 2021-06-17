# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib3
import re
import pandas as pd

'''
Para leer una pagina .aspx
''' 
url = 'https://www.camara.cl/legislacion/sala_sesiones/asistencia_resumen.aspx'
http = urllib3.PoolManager()
r = http.request('get', url)
soup = BeautifulSoup(r.data, 'lxml')


'''
Lecura de la tabla
'''
tabla = soup.find('table',class_='tabla')
filas = tabla.find_all('tr',text=False)

# print(filas[2].prettify())
listNombreDiputado = list()
listPartido =list()
listAsistencia = list()
listSinJustificacion = list()
listPorcAsistencia = list()

listJustificacionSiAfectaPorcDic = list()
listJustificacionNoAfectaPorcDic = list()

afectaDic = dict()
noAfectaDic = dict()

swMain = True
indiceMain=1
while swMain:
    
    
    '''
    este indice maneja cada fila de la tabla, el indice no se controla
    de forma incremental, esta determinado por todos los elementos td de la tabla, 
    ademas, dado como esta construida la pagian, las tablas tienen tablas dentro sin ningun identificador, 
    por lo mismo el indice que controla de forma manual.
    '''
    fila = filas[indiceMain]#58
    # print(fila)
    
    '''
    Datos de facil acceso sin tablas dentro
    '''
    nombreDiputado = fila.find_all('td')[0].text.strip()
    partido = fila.find_all('td')[1].text.strip()
    asistencia = fila.find_all('td')[2].text.strip()
    sinJustificacion = fila.find_all('td')[-2].text.strip()
    porcAsistencia = fila.find_all('td')[-1].text.strip()
    justificacionNoAfectaPorc = fila.find_all('td')[3].div.a.span.text.strip()
    
   
    swExit = True
    indice = 4
    
    '''
    Declaracion de diccionarios para obtener justificaciones
    '''
    justificacionNoAfectaPorcDic= dict()
    justificacionSiAfectaPorcDic = dict()
    
    while (swExit):
        
        x = re.search("Justificaciones que SÍ afectan", fila.find_all('td')[indice].text)
        
        if x!= None:
            '''
            Encontre elemento HTML que posee
            Justificaciones que SÍ afectan
            '''
            tabla = fila.find_all('table')
            '''
            Reviso si las justificaciones son mayor a 0 para poder recorrer la tabla
            '''
            justificacionesSiMayor0 = int(fila.find_all('td')[indice].find('span').text)
            indiceTabla = len(tabla)-1
            if(justificacionesSiMayor0 > 0 and len(tabla) > 0):
                indice2 = 0
                while (indice2<len(tabla[indiceTabla].find_all('td'))):
                    justificacionSiAfectaPorcDic[tabla[indiceTabla].find_all('td')[indice2].text.strip()] = tabla[indiceTabla].find_all('td')[indice2 +1].text.strip()
                    indice2= indice2 + 2
            swExit = False
        else:
            justificacionNoAfectaPorcDic[fila.find_all('td')[indice].text.strip()] = fila.find_all('td')[indice +1].text.strip()
        indice= indice + 2
    '''
    Fin while anidado
    '''
    
    # determianr la cantidad de asistenica a partir de los diccionarios
    if (len(justificacionSiAfectaPorcDic)==0):
        listJustificacionSiAfectaPorcDic.append(0)
    else:
        #Suma del diccionario justificacion no Afecta Porcetaje diario
        listJustificacionSiAfectaPorcDic.append( sum([ int(value) for value in justificacionSiAfectaPorcDic.values()] ))
    
    if (len(justificacionNoAfectaPorcDic)==0):
        listJustificacionNoAfectaPorcDic.append(0)
    else:
        #Suma del diccionario justificacion no Afecta Porcetaje diario
        listJustificacionNoAfectaPorcDic.append( sum([ int(value) for value in justificacionNoAfectaPorcDic.values()] ))    
    
    #control del indice maestro y evaluacion salida ciclo while
    indiceMain = indiceMain + len(justificacionSiAfectaPorcDic) + len(justificacionNoAfectaPorcDic) + 1
    if (indiceMain >=len(filas)):
        swMain= False

      #Asignacion de campos a listas para construir dataframe mas adelante
    listNombreDiputado.append(nombreDiputado)
    listPartido.append(partido)
    listAsistencia.append(asistencia)
    listSinJustificacion.append(sinJustificacion)
    listPorcAsistencia.append(porcAsistencia)
    noAfectaDic[nombreDiputado] = justificacionNoAfectaPorcDic
    afectaDic[nombreDiputado] = justificacionSiAfectaPorcDic


#Armar dataframe asistencia
dfAsistenciaDiputados = pd.DataFrame(list(zip(listNombreDiputado, 
                                            listPartido,
                                            listAsistencia,
                                            listSinJustificacion,
                                            listPorcAsistencia,
                                            listJustificacionNoAfectaPorcDic,
                                            listJustificacionSiAfectaPorcDic)),
                                    columns = ["nombreDiputado",
                                              "partido",
                                              "asistencia",
                                              "sinJustificacion",
                                              "porcentajeAsistencia",
                                              "justificacionNoAfectaPorcentaje",
                                              "justificacionSiAfectaPorcentaje"])

afeNombreDiputadoList = list()
afeNombreCausaList = list()
afeNombreCantidadList = list()
#Armar dataframe justificaciones que afectan
for llave in afectaDic.keys():
    for llaveCausa in afectaDic[llave].keys():
        afeNombreDiputadoList.append(llave)
        afeNombreCausaList.append(llaveCausa)
        afeNombreCantidadList.append(int(afectaDic[llave][llaveCausa]))  
dfJustAfeAsi = pd.DataFrame(list(zip(afeNombreDiputadoList, 
                                      afeNombreCausaList,
                                      afeNombreCantidadList)),
                            columns = ["nombreDiputado",
                                        "causa",
                                        "cantidad"])    

noAfeNombreDiputadoList = list()
noAfeNombreCausaList = list()
noAfeNombreCantidadList = list()
#Armar dataframe justificaciones que NO afectan
for llave in noAfectaDic.keys():
    for llaveCausa in noAfectaDic[llave].keys():
        noAfeNombreDiputadoList.append(llave)
        noAfeNombreCausaList.append(llaveCausa)
        noAfeNombreCantidadList.append(int(noAfectaDic[llave][llaveCausa]))

dfJustNoAfeAsi = pd.DataFrame(list(zip(noAfeNombreDiputadoList, 
                                            noAfeNombreCausaList,
                                            noAfeNombreCantidadList)),
                                    columns = ["nombreDiputado",
                                              "causa",
                                              "cantidad"])

'''

Fin web Scrapping y generacion de dataframes ASISTENCIA
    dfAsistenciaDiputados
    dfJustAfeAsi
    dfJustNoAfeAsi
*******************************************************************************  
'''




'''
Para leer una pagina .aspx
''' 
url = 'https://www.camara.cl/diputados/diputados.aspx'
r = http.request('get', url)
soup = BeautifulSoup(r.data, 'lxml')

'''
Lecura del div contenedor de la informacion
'''
mainDiv = soup.find('div',id='ContentPlaceHolder1_ContentPlaceHolder1_pnlDiputadosLista')
articulos = mainDiv.find_all('article',text=False)

listnomDiputado = list()
listDistrito = list()
listPartido = list()
listcontacto = list()
for articulo in articulos:
    
    listnomDiputado.append(articulo.find('h4').a.text)
    listDistrito.append(articulo.find_all('p')[0].text)
    listPartido.append(articulo.find_all('p')[1].text)
    listcontacto.append(articulo.find_all('a')[2]['href'])

dfDiputadoDistrito = pd.DataFrame(list(zip(listnomDiputado, 
                                            listDistrito,
                                            listPartido,
                                            listcontacto)),
                                    columns = ["nombreDiputado",
                                              "distrito",
                                              "partido",
                                              "contacto"])

'''

Fin web Scrapping y generacion de dataframes DISTRITO
    dfDiputadoDistrito

*******************************************************************************  
'''


'''

Preparar dataSet para unir
Antes de eso se debe estandarizar el nombre de df asistencia a los de distrito.

'''
def normalizarNombre(valor):
    prefijo = re.search('Sr[.a]', valor)
    textPrefijo = valor[prefijo.start(): prefijo.end()]
    if (textPrefijo == 'Sra'):
        textPrefijo = textPrefijo + '.'
    reApm = re.search('\s.[.]\s', valor)
    textApellido = valor[prefijo.end()+1  : reApm.start()].strip()
    textNombre = valor[reApm.end(): len(valor)]
    return("{} {} {}".format(textPrefijo, textNombre, textApellido))
dfAsistenciaDiputados['nombreDiputado'] = dfAsistenciaDiputados['nombreDiputado'].apply(normalizarNombre)

dfFinal = pd.merge(dfDiputadoDistrito, dfAsistenciaDiputados, on="nombreDiputado")    
'''
*******************************************************************************  

                        P R E P R O C E S A M I E N T O

*******************************************************************************  
'''
'''
Limipar campo partido_X
'''
def eliminaPartido(valor):
    return(valor[9:len(valor)])
dfFinal['partido_x'] = dfFinal['partido_x'].apply(eliminaPartido)
'''
Limipar campo distrito
'''
def limpiaDistrito(valor):
    return(valor[12:len(valor)])
dfFinal['distrito'] = dfFinal['distrito'].apply(limpiaDistrito)

def limpiaConcacto(valor):
    valor = valor.replace("mailto:", "")
    valor = valor.replace("?subject=Consulta", "")
    return(valor)
dfFinal['contacto'] = dfFinal['contacto'].apply(limpiaConcacto)


def limpiarPorcentajeAsistencia(valor):
    valor = valor.replace(" %", "")
    valor = valor.replace(",", ".")
    valor = float(valor)/100
    return(valor)
dfFinal['porcentajeAsistencia'] = dfFinal['porcentajeAsistencia'].apply(limpiarPorcentajeAsistencia)


'''
Guardar dataframes
'''
dfFinal.to_json(r'Diputados.json')
dfJustAfeAsi.to_json(r'justificacionSiAfectaAsistencia.json')
dfJustNoAfeAsi.to_json(r'justificacionNoAfectaAsistencia.json')



