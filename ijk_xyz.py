#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 22:04:32 2021

@author: lastdon
"""
import pandas as pd

df = pd.read_csv (r'/home/lastdon/Documents/SG9015.csv')
print (df)
df['xcentre'] = (df['IX']*15)+162533.094
df['ycentre'] = (df['IY']*15)+4469346.5
df['zcentre'] = (df['IZ']*16)+648
df.to_csv('SG9015_NG.csv', sep=',', index=False)