# -*- coding: utf-8 -*-
#######################################################
#filename:xlrd_draw.py
#author:
#date:xxxx-xx-xx
#function：读excel文件中的数据
#######################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import xlrd
import plotly.plotly as py

font = {'family': 'serif',
        'color':  'red',
        'weight': 'normal',
        'size': 10,
        }
#打开一个workbook
# # print ('Please Input the Excel name Without XLS:')
Wname = raw_input('Please Input the Excel name Without XLS:')
# #print('worksheets is %s' %Wname)
# workbook = xlrd.open_workbook(Wname + '.csv')

df = pd.read_csv(Wname + ".csv", header=0)
#print df['DN']
# plt.subplot(1, 2, 1)
df.plot(x='Length', y='B1')
# plt.subplot(1, 2, 2)
# df.plot(x='Length', y='B2')
# df.plot(x='Length', y='B3')
# df.plot(x='Length', y='B4')
# plt.legend(hide)
plt.show()


'''
#抓取所有sheet页的名称
worksheets = workbook.sheet_names()
# print('worksheets is %s' %worksheets)

#定位到mySheet
mySheet = workbook.sheet_by_index(0)
LabelX = mySheet.name
# mySheet1 = workbook.sheet_by_name(u'Spectral Response_S2A')
#get rows, cols
nrows=mySheet.nrows
ncols=mySheet.ncols
# nrows1=mySheet1.nrows
# ncols1=mySheet1.ncols
# Get Title
labels = mySheet.row_values(0)
# labels_1 = mySheet1.row_values(0)
# print labels
#get datas

# plt.grid(True)
x = mySheet.col_values(0, start_rowx=2, end_rowx=None)
# x1 = mySheet1.col_values(0, start_rowx=2, end_rowx=None)
# print x
T_value = input('Please Input the Binary Thresholding Value:')
for i in range(ncols-1):
	y=mySheet.col_values(i+1, start_rowx=2, end_rowx=None)
	label='label' + str(i)
	plt.plot(x,y,linestyle='solid',linewidth=0.5, markerfacecolor='g', markersize=6,label=labels[i+1] )
# 划分界限
plt.axvline(T_value, ymin=0.0, ymax = 55000, linewidth=1, color='k')
# 标注
plt.text(T_value+0.1, 30000, r'Built-up', fontdict=font)
plt.text(T_value-0.4, 30000, r'Non Built-up', fontdict=font)
# for i in range(ncols1-1):	
	# y1=mySheet1.col_values(i+1, start_rowx=2, end_rowx=None)
	# label='label' + str(i)
	# plt.plot(x1,y1,linestyle='solid',linewidth=0.5, color='blue',markerfacecolor='g', markersize=6,label=labels_1[i+1])
	# #line2,= plt.plot(x1,y1,linestyle='solid',linewidth=0.5, color='blue',markerfacecolor='g', markersize=6,label='label2')

# plt.legend()

#plt.legend(handles=[line1,line2], loc=1)


#plt.legend([line1, line2], ['label1', 'label2'])

plt.xlabel(LabelX)
plt.ylabel('Pixcel Count')
plt.show()



x = mySheet.col_values(0, start_rowx=1, end_rowx=None)
y1 = mySheet.col_values(1, start_rowx=1, end_rowx=None)
y2 = mySheet.col_values(2, start_rowx=1, end_rowx=None)
y3 = mySheet.col_values(3, start_rowx=1, end_rowx=None)
y4 = mySheet.col_values(4, start_rowx=1, end_rowx=None)
# Create traces
# trace1 = go.Scatter(
    # x = x,
    # y = y1,
    # mode = 'lines+markers',
    # name = 'lines+markers'
# )
# trace2 = go.Scatter(
    # x = x,
    # y = y2,
    # mode = 'lines+markers',
    # name = 'lines+markers'
# )
# data = [trace1, trace2]
# plt.scatter(x, y1)
plt.grid(True)
plt.plot(x,y1,color='g', linestyle='solid', marker='o', markerfacecolor='g', markersize=6)
plt.plot(x,y2,color='b', linestyle='solid', marker='v', markerfacecolor='b', markersize=6)
plt.plot(x,y3,color='r', linestyle='solid', marker='^', markerfacecolor='r', markersize=6)
plt.plot(x,y4,color='c', linestyle='solid', marker='<', markerfacecolor='c', markersize=6)
plt.xlabel('Wavelegth)(um)')
plt.ylabel('Reflentance')
# plt.hist(x,y1)
# plt.scatter(x, y2)

# plt.plot(data, filename='line-mode')
plt.show()
# #time = mySheet.col(1)
# #time = [x.value for x in time]


# #drop the 1st line of the data, which is the name of the data.
# pressure.pop(0)
# #time.pop(0)

# #declare a figure object to plot
# fig = plt.figure(1)

# #plot pressure
# plt.plot(pressure)
 
# plt.title('Barometer') 
# plt.ylabel('Pa') 
# #plt.xticks(range(len(time)),time) 
# plt.show()
'''