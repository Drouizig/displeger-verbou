#!/bin/python3
import sys
import csv
import operator

reader = csv.reader(open(sys.argv[1]), delimiter=";")
writer = csv.writer(sys.stdout, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

next(reader)
sortedlist = sorted(reader, key = operator.itemgetter(2,0,1), reverse=False)
print("anv_verb;diaz_verb;rummad;galleg;saozneg")
for row in sortedlist:
    writer.writerow(row)