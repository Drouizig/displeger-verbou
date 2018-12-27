#!/bin/python3
import sys

verbs_categories = ['a1', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6']
ANV_VERB = 0
DIAZ_VERB = 1
RUMMAD = 2
GALLEG = 3
SAOZNEG = 4

#dibennoù verb dre rummad. Pouezus eo mirout an urzh
dibennou = {
    'd5' : ['liañ', 'liout', 'liet', 'liezh'],
    'd6' : ['niañ', 'niout', 'niet', 'niezh'],
    'd4' : ['iañ', 'iout', 'iet', 'iezh'],
    'd1' : ['añ', 'iñ', 'out', 'et', 'ezh', 'at'],
    'd3' : ['a']
}

nemedennou = ['aliañ', 'gouzout']

def getRummad(anvverb):
    for rummad in dibennou:
        for dibenn in dibennou[rummad]:
            if anvverb.endswith(dibenn) and anvverb not in nemedennou:
                return rummad
    return 'd1'

def getPennrann(rummad, anvverb, diazverb):
    dibenn = findDibenn(anvverb, rummad)
    if len(dibenn) == 0:
        return anvverb
    else:
        return anvverb[:-1*len(dibenn)]
    
    
def findDibenn(anvverb, rummad):
    for dibenn in dibennou[rummad]:
        if anvverb.endswith(dibenn):
            return dibenn
    return ''

with open(sys.argv[1]) as f:
    for line in f:
        lineData = line.split(';')
        anvverb = lineData[ANV_VERB]
        diazVerb = lineData[DIAZ_VERB]
        rummad = lineData[RUMMAD]
        galleg = lineData[GALLEG]
        saozneg = lineData[SAOZNEG]
        newRummad = rummad
        newPennrann = diazVerb
        if rummad == 'a1':
            newRummad = getRummad(anvverb)
            if diazVerb == '#pennrann':
                newPennrann = getPennrann(newRummad,anvverb,diazVerb)
            if newRummad == 'd1' and newPennrann.endswith(('a', 'eu', 'o')):
                newRummad = 'd2'
            
        print('%s;%s;%s;%s;%s' % (anvverb, newPennrann, newRummad, galleg, saozneg.replace('\n', '')))
