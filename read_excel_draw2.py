# -*- coding: utf-8 -*-
#######################################################
#filename:xlrd_draw.py
#author:
#date:xxxx-xx-xx
#function：读excel文件中的数据
#######################################################
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import xlrd
import plotly.plotly as py
#打开一个workbook
workbook = xlrd.open_workbook('test1.xls')
 
#抓取所有sheet页的名称
worksheets = workbook.sheet_names()
print('worksheets is %s' %worksheets)
 
#定位到mySheet
mySheet = workbook.sheet_by_name(u'Spectral Response_LC8')
mySheet1 = workbook.sheet_by_name(u'Spectral Response_S2A')
#get rows
nrows=mySheet.nrows
labels = mySheet.row_values(0)
labels_1 = mySheet1.row_values(0)

ncols=mySheet.ncols

nrows1=mySheet1.nrows
ncols1=mySheet1.ncols
# print nrows
#get datas

# plt.grid(True)
x = mySheet.col_values(0, start_rowx=2, end_rowx=None)
x1 = mySheet1.col_values(0, start_rowx=2, end_rowx=None)
plt.subplot(2, 1, 1)
for i in range(ncols-1):
	y=mySheet.col_values(i+1, start_rowx=2, end_rowx=None)
	label='label' + str(i)
	plt.plot(x,y,linestyle='dashed',linewidth=0.5, markerfacecolor='g', markersize=6,label=labels[i+1] )
plt.legend()
plt.subplot(2, 1, 2)
for i in range(ncols1-1):	
	y1=mySheet1.col_values(i+1, start_rowx=2, end_rowx=None)
	label='label' + str(i)
	plt.plot(x1,y1,linestyle='solid',linewidth=0.5, color='blue',markerfacecolor='g', markersize=6,label=labels_1[i+1])
	#line2,= plt.plot(x1,y1,linestyle='solid',linewidth=0.5, color='blue',markerfacecolor='g', markersize=6,label='label2')
plt.legend()

#plt.legend(handles=[line1,line2], loc=1)


#plt.legend([line1, line2], ['label1', 'label2'])

plt.xlabel('Wavelegth)(um)')
plt.ylabel('Reflentance')
plt.show()


'''	
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