#!/usr/bin/env python
'''
JSON XML [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Johana Rangel"
__email__ = "johanarang@hotmail.com"
__version__ = "1.1"


import json
import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec

def ej1():
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede inventar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    json_data = {
                "Nombre": "Cristina",
                "Apellido": "Vega",
                "Dni": 95000001,
                "Ropa": [
                         {"Prendas": "Sweter", "Cantidad": 3},
                         {"Prendas": "Blusas", "Cantidad": 10},
                         {"Prendas": "Camperas", "Cantidad": 2}
                        ]

                }
    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    # Observe el archivo y verifique que se almaceno lo deseado
    with open('json_data.json', 'w') as jsonfile:
        data = [json_data]
        json.dump(data, jsonfile, indent=4)


def ej2():
    # JSON Deserialize
    # Basado en el ejercicio anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en el ej1
    
    with open('json_data.json', 'r') as jsonfile:
        data = json.load(jsonfile)

        json_string = json.dumps(data, indent=4)
        print(json_string) #SE VE IGUAL COMO EN EL ARCHIVO, PERO EN CONSOLA.

   
def ej3():
    # Ejercicio de XML
    # Basado en la estructura de datos del ejercicio 1,
    # crear a mano un archivo ".xml" y generar una estructura
    # lo más parecida al ejercicio 1.
    # El objectivo es que armen un archivo XML al menos
    # una vez para que entiendan como funciona.
    
  
    # with open('datosPersonales.xml', 'w') as xmlfile:
    #     datos_personales = ET.Element("datos_personales")
        
    #     datos_personales1 = ET.SubElement(datos_personales, "nombre").text = "Cristina"
    #     datos_personales2 = ET.SubElement(datos_personales, "apellido").text = "Vega"
    #     datos_personales3 = ET.SubElement(datos_personales, "dni").text = "95000001"
    #     datos_personales4 = ET.SubElement(datos_personales, "ropa").text = "Ropa"
               
    #     ET.dump(datos_personales)
    #     tree = ET.ElementTree(datos_personales)
    #     tree.write('datosPersonales.xml')
    pass
    

def ej4():
    # XML Parser
    # Tomar el archivo realizado en el punto anterior
    # e iterar todas las tags del archivo e imprimirlas
    # en pantalla tal como se realizó en el ejemplo de clase.
    # El objectivo es que comprueben que el archivo se realizó
    # correctamente, si la momento de llamar al ElementTree
    # Python lanza algún error, es porque hay problemas en el archivo.
    # Preseten atención al número de fila y al mensaje de error
    # para entender que puede estar mal en el archivo.
    
    tree = ET.parse('datosPersonales.xml')
    root = tree.getroot()

    for child in root:
        print('tag:', child.tag, 'attr:', child.attrib, 'text:', child.text)
        for child2 in child:
            print('tag:', child2.tag, 'attr:', child2.attrib, 'text:', child2.text)

def filtrar(usuario):

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    dataset = response.json()

    filter_data = [x for x in dataset if x.get('completed') is True]
    return [x for x in filter_data if x.get('userId') == usuario]

def ej5():
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general.
    # Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".

    # De cada usuario en el total de las 200 entradas contar cuantos títulos
    # completó cada usuario (de los 10 posibles) y armar
    # un gráfico de torta resumiendo la información.

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de torta.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    data_usuario1 = filtrar(usuario=1)
    data_usuario2 = filtrar(usuario=2)
    data_usuario3 = filtrar(usuario=3)
    data_usuario4 = filtrar(usuario=4)
    data_usuario5 = filtrar(usuario=5)
    data_usuario6 = filtrar(usuario=6)
    data_usuario7 = filtrar(usuario=7)
    data_usuario8 = filtrar(usuario=8)
    data_usuario9 = filtrar(usuario=9)
    data_usuario10 = filtrar(usuario=10)

    completados = {'user1': len(data_usuario1),
                   'user2': len(data_usuario2),
                   'user3': len(data_usuario3),
                   'user4': len(data_usuario4),
                   'user5': len(data_usuario5),
                   'user6': len(data_usuario6),
                   'user7': len(data_usuario7),
                   'user8': len(data_usuario8),
                   'user9': len(data_usuario9),
                   'user10': len(data_usuario10),
                    }
    
    fig = plt.figure('Gráfico Pie')
    fig.suptitle('"Títulos completados por el usuario"', fontsize=16)
    ax = fig.add_subplot()

    explode = (0.1, 0, 0, 0, 0, 0, 0,0,0,0)

    ax.pie(completados.values(), labels=completados.keys(), explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')

    plt.show()
    

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
