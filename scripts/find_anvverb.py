#!/bin/python3
import sys

ANV_VERB = 0
DIAZ_VERB = 1
RUMMAD = 2
GALLEG = 3
SAOZNEG = 4

#dibennoù verb dre rummad. Pouezus eo mirout an urzh
dibennou = ['añ', 'iñ', 'out', 'et', 'ezh', 'at', 'al']

dic= []

with open('br_FR.dic') as fdic:
    for linedic in fdic:
        linedic = linedic.strip('\n')
        linedic = linedic.replace('/a0 ', '')
        dic.append(linedic)

with open(sys.argv[1]) as f:
    for line in f:
        lineData = line.split(';')
        anvverb = lineData[ANV_VERB]
        diazVerb = lineData[DIAZ_VERB]
        rummad = lineData[RUMMAD]
        galleg = lineData[GALLEG]
        saozneg = lineData[SAOZNEG]

        if anvverb == '#anv-verb':
            anviouverb = []
            for linedic in dic:
                for dibenn in dibennou:
                    if linedic == (diazVerb + dibenn):
                        anviouverb.append(linedic.strip('\n'))
            if len(anviouverb) > 0:
                for a in anviouverb:
                    print('%s;%s;%s;%s;%s' % (a, diazVerb, rummad, galleg, saozneg.replace('\n', '')))
            else:
                print(line.replace('\n', ''))
        else:
            print(line.replace('\n', ''))