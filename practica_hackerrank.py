#!/usr/bin/env python

import requests
import json
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec
import re
from collections import defaultdict


def fetch(page_number, location_id):

    url = 'https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page={}.format(page_number)'
    response = requests.get(url)
    data_info = response.json()


    data = [{'userId': x['userId'], 'amount': x['amount'], 'location':x['location']['id']} for x in data_info['data'] if x['location']['id'] == location_id]

    return [{'userId': x['userId'], 'amount': x['amount']} for x in data]
    

def transform(dataset):

    usuario = [x for x in dataset if x['userId'] and x['amount']]
    
        
    resultado = {}
    key_userId = 'userId'

    for dct in usuario:
        userId_val = dct.pop(key_userId)
        resultado.setdefault(userId_val, {key_userId: userId_val})
        for k, v in dct.items():
            resultado[userId_val][k] = resultado[userId_val].get(k, 0) + float(re.sub(r'[^\d\-.]', '', v))
    return resultado  
      
def report(data):
    
    x = [x for x in data.keys()]
    y = [x.get('amount') for x in data.values()] 
    
    fig = plt.figure('Reporte')
    fig.suptitle('"Débito total por usuario"', fontsize=16)
    ax = fig.add_subplot()
    
    ax.bar(x, y, color= 'darkgreen')
    ax.set_facecolor('white')
    ax.set_ylabel("[Débito total]")
    ax.set_xlabel("[Usuario]")
    ax.legend()
    plt.show()
    
    
if __name__ == "__main__":

    dataset = fetch(page_number=1, location_id=7)
    data = transform(dataset)
    report(data)