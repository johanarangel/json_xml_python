#!/usr/bin/env python

import requests
import json
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec


def fetch():

    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'
    response = requests.get(url)
    data = response.json()
    return [{'price': x['price'], 'condition':x['condition']} for x in data['results'] if x['currency_id'] == "ARS"] 
   

def transform(dataset, min, max):
      
    depa_minparametro = [x for x in dataset if x['price'] <= min]

    depa_promedio = [x for x in dataset if min < x['price'] < max]

    depa_maxparametro = [x for x in dataset if x['price'] >= max]

    min_count = len(depa_minparametro)
    min_max_count = len(depa_promedio)
    max_count = len(depa_maxparametro)

    data = [min_count, min_max_count, max_count]
    return data

def report(data):

    leyenda = ['Mínimo', 'Promedio', 'Máximo']
    
    fig = plt.figure('Reporte')
    fig.suptitle('"Alquileres en Mendoza"', fontsize=16)
    ax = fig.add_subplot()

    explode = (0.1, 0, 0)

    ax.pie(data, labels=leyenda, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')

    plt.show()

    
    
if __name__ == "__main__":
    
    min = 10000
    max = 30000

    dataset = fetch()
    data = transform(dataset, min, max)
    report(data)