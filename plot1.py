# -*- coding: utf-8 -*-
# and must use &
import matplotlib  # 导入matplotlib库
from numpy import *
import pandas as pd
import numpy as np
import xdrlib, sys
import matplotlib.pyplot as plt

# open excel file and get sheet
data = pd.read_excel('test1.xls', 'Spectral Response_LC8')

# get datas
# print data['B8']
# x = data['B8'].head(1500)
# y= data['B2'].head(1500)
print (data.loc[0:3, ['B1', 'B2']])

# x = data['length']
# y= data['DN']
# y = x [x.B2 >=0]
# print (x)
# print (y)
# y= data['B2'] > 0

# print (x)
# print (y)
# x1 = x['B8']#.head(1500)
# y1 = x['B2']#.head(1500)
# print (x1)
# print (y1)
plt.figure(figsize=(10, 10), dpi=98)

plt.subplot(311)
plt.title('A tale of 1 subplots')
plt.ylabel('Damped oscillation')
plt.plot(data['Length'], data['B1'], "g-", label='CA')
plt.plot(data['Length'], data['B2'])
plt.plot(data['Length'], data['B3'])
plt.plot(data['Length'], data['B4'])
plt.grid()
plt.xlabel('Wavelength(um)')
plt.legend()
plt.subplot(312)
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation111')
plt.plot(data['Length'], data['B5'])
plt.plot(data['Length'], data['B6'])
plt.plot(data['Length'], data['B7'])
plt.plot(data['Length'], data['B8'])
plt.xlabel('Wavelength(um)')
plt.grid(color='k', linewidth=1, linestyle='-')

plt.subplot(313)
plt.scatter(data['B2'], data['B3'])

plt.show()
