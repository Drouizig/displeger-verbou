#!/bin/python3
import sys
verbs_categories = ['a1', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6']

print("anvverb;diaz;rummad")
with open('br.dic') as f:
   for line in f:
       if any(ext in line for ext in verbs_categories):
          verbData = line.replace('a0', '').split('/')
          diaz = verbData[0]
          anvverb = diaz
          rummad = 'a1'
          if verbData[1] == 'a1':
              anvverb = diaz + "añ"
          elif verbData[1].startswith('d'):
              if(verbData[1].startswith('d2d3'):
                  rummad = 'd3'
              else:
                  rummadData = verbData[1].split(' ')
                  rummad = rummadData[0]
