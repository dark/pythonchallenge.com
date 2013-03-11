#!/usr/bin/python
# http://www.pythonchallenge.com/pc/def/peak.html

import pickle

f = open('05.data/banner.p', 'r')
obj = pickle.load(f)

for row in obj:
    for column in row:
        # column is a tuple like (' ', 2)
        for x in range(column[1]) :
            print column[0] ,
    print
