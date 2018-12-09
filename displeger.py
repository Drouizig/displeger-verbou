#!/bin/python3
import sys
import json

ANV_VERB = 0
DIAZ_VERB = 1
RUMMAD = 2
GALLEG = 3

verb = sys.argv[1]

raganvioù = ['U1', 'U2', 'U3', 'L1', 'L2', 'L3', 'D ']


displeg = json.load(open('verbou.json'))


def printAmzer(diazVerb, dibennou):
    i = 0
    for dibenn in dibennou:
        if dibenn.__class__ == list:
            print(raganvioù[i]+'. ')
            for dib in dibenn:
                print(diazVerb+dib+', pe ')
        elif dibenn.__class__ == str:
            print(raganvioù[i]+'. '+diazVerb+dibenn)
        i += 1

with open('displeger_format.csv') as f:
   for line in f:
       if line.startswith(verb+';'):
            lineData = line.split(';')
            rummad = lineData[RUMMAD]
            diazVerb = lineData[DIAZ_VERB]
            galleg = lineData[GALLEG]
            print(verb)
            print('################################')
            print('\n')
            print('Amzer a-vremañ')
            printAmzer(diazVerb, displeg[rummad]['bremañ'])
            print('')
            print('Amzer tremenet ledan')
            printAmzer(diazVerb, displeg[rummad]['tremenet_ledan'])

            print('')
            print('Amzer tremenet strizh')
            printAmzer(diazVerb, displeg[rummad]['tremenet_strizh'])

            print('')
            print('Amzer da zont')
            printAmzer(diazVerb, displeg[rummad]['da_zont'])

            print('')
            print('Gallus')
            printAmzer(diazVerb, displeg[rummad]['gallus'])

            print('')
            print('Dic\'hallus')
            printAmzer(diazVerb, displeg[rummad]['dichallus'])

            print('')
            print('Kadarnaat')
            printAmzer(diazVerb, displeg[rummad]['kadarnaat'])
