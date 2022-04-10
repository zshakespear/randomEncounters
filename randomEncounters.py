# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 09:34:31 2022

@author: zacos

I'm experimenting with the idea of using a simple program
to handle random encounters using excel sheets
"""

import os
import pandas as pd
import random as r

wd = os.getcwd()
it = 0
dirpd = pd.DataFrame(columns = ['file'])

for files in os.listdir(wd):
    newdirpd = pd.DataFrame([[files]], columns = ['file'])
    dirpd = pd.concat([dirpd, newdirpd],ignore_index=True)
    it += 1

print(dirpd.to_string())

regin = input('Please select the index of the file you would like to open\n')
regin = int(regin)

#In a later iteration I would like to fix the dataframe so that the column
#names actually match
encdir = dirpd.at[regin, 'file']

tabledir = wd + '\\' + encdir

randtable = pd.read_excel(tabledir)

season = input('Please select the season: \n0: Spring\n1: Summer\n2: Fall\n3: Winter\n')
season = int(season)
if season == 0:
    season = 'Spring'
else:
    if season == 1:
        season = 'Summer'
    else:
        if season == 2:
            season = 'Fall'
        else:
            season = 'Winter'

srandtable = randtable[season]
srandtable = srandtable[srandtable.notna()]

randlim = srandtable.size - 1
seed = r.randint(0, randlim)

print(srandtable[seed])
