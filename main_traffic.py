# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 14:53:14 2019

@author: amrob
"""

import pandas as pd 
from Traffic_View_Class import Traffic_View as TV


filename = 'Daily Turnstile 3.xlsx'
sheetname1 = 'November'
sheetname2 = 'December '

Traffic_Nov = TV.Clean_Traffic(filename, sheetname1)
Traffic_Dec = TV.Clean_Traffic(filename, sheetname2)


Traffic_Nov_Dec = TV.appending_months(Traffic_Nov, Traffic_Dec)
print(Traffic_Nov_Dec)

Traffic_Nov_Dec.to_csv('Traffic_November_December.csv')
