#!/bin/python3
import sys

ANV_VERB = 0
PENNRANN = 1
RUMMAD = 2
GALLEG = 3
SAOZNEG = 4
c1 = 0
toDelete = []
checked = []
with open(sys.argv[1]) as f:
    for line in f:
        c1 += 1
        lineData = line.split(';')
        pennrann = lineData[PENNRANN]
        anvverb = lineData[ANV_VERB]
        c2 = 0
        if len(pennrann) != 0 and c1 not in checked:
            with open(sys.argv[1]) as f2:
                for line2 in f2:
                    c2 += 1
                    lineData2 = line2.split(';')
                    pennrann2 = lineData2[PENNRANN]
                    anvverb2 = lineData2[ANV_VERB]
                    if pennrann == pennrann2 and c1 != c2 and (anvverb == "#anv-verb" or anvverb2 == "#anv-verb" or anvverb == anvverb2):
                        score1 = 5 -line.count('#')
                        score2 = 5 -line2.count("#")
                        #print("line "+ str(c1) + " : " + line.strip('\n') + ', score : ' + str(score1))
                        #print("line "+ str(c2) + " : " + line2.strip('\n') + ', score : ' + str(score2))
                        #print('#######')
                        checked.append(c2)
                        if score1 < score2:
                            toDelete.append(c1)
                        else:
                            toDelete.append(c2)
#print('total : ' + str(len(toDelete)))

c = 0
with open(sys.argv[1]) as f:
    for line in f:
        c += 1
        if c not in toDelete:
            print(line.strip('\n'))