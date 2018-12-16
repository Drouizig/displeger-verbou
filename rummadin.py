#!/bin/python3
import sys

verbs_categories = ['a1', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6']
ANV_VERB = 0
DIAZ_VERB = 1
RUMMAD = 2
GALLEG = 3
SAOZNEG = 4

with open('displeger_format.csv') as f:
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
            if anvverb.endswith('liañ'):
                newRummad = 'd5'
                if diazVerb == '#pennrann':
                    newPennrann = anvverb.replace('liañ', '')
            elif anvverb.endswith('niañ'):
                newRummad = 'd6'
                if diazVerb == '#pennrann':
                    newPennrann = anvverb.replace('niañ', '')
            elif anvverb.endswith('iañ'):
                newRummad = 'd4';
                if diazVerb == '#pennrann':
                    newPennrann = anvverb.replace('iañ', '')
            elif anvverb.endswith('a'):
                newRummad = 'd3';
                if diazVerb == '#pennrann':
                    newPennrann = anvverb.replace('a', '')
            elif diazVerb.endswith(('a', 'eu', 'o')):
                newRummad = 'd2';
            else:
                newRummad = 'd1';
                if diazVerb == '#pennrann':
                    if anvverb.endswith('añ'):
                        newPennrann = anvverb.replace('añ', '')
                    elif anvverb.endswith('iñ'):
                        newPennrann = anvverb.replace('iñ', '')
        print('%s;%s;%s;%s;%s' % (anvverb, newPennrann, newRummad, galleg, saozneg.replace('\n', '')))
