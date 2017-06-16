"""
Otsu thresholding
==================

This example illustrates automatic Otsu thresholding.
"""

import matplotlib.pyplot as plt
from skimage import data
try:
    from skimage import filters
except ImportError:
    from skimage import filter as filters
from skimage import exposure
from scipy import optimize
import numpy as np
import gdal
#import pandas as pd


def matrix_lstsqr(x, y):
    X = np.vstack([x, np.ones(len(x))]).T
    return (np.linalg.inv(X.T.dot(X)).dot(X.T)).dot(y)

def f_1(x, A, B):
    return A*x + B

ds1 = gdal.Open("./S2A.dat")
ds2 = gdal.Open("./LC8.dat")
camera1 = np.array(ds1.GetRasterBand(3).ReadAsArray())

#camera11 = camera.flatten()
camera11 = camera1.flatten()
camera11 = [i for i in camera11 if (i>=0 and i<=1)]
camera11 = np.asarray(camera11)

camera2 = np.array(ds2.GetRasterBand(3).ReadAsArray())
camera21 = camera2.flatten()
camera21 = [i for i in camera21 if (i>=0 and i<=1)]
camera21 = np.asarray(camera21)
#camera = data.camera()
plt.scatter(camera11,camera21,s= 1)

x0 = camera11
y0 = camera21
#A1, B1 = optimize.curve_fit(f_1, x0, y0)[0]
A1, B1 = matrix_lstsqr( x0, y0)
x1= x0
y1= A1*x1 + B1
plt.plot(x1, y1, "blue")

ftext = 'y =  {:.3f} + {:.3f}x'.format(A1, B1)
plt.figtext(.15,.8, ftext, fontsize=11, ha='left')
plt.figtext(0.6,.2, "Red", fontsize=11, ha='left')
plt.ylabel('Landsat-8 OLI/TIRS')
plt.xlabel('Sentinel-2 MSI')
plt.tight_layout()
plt.show()






plt.scatter(camera11,camera21,s= 1)

x0 = camera11
y0 = camera21
#A1, B1 = optimize.curve_fit(f_1, x0, y0)[0]
A1, B1 = matrix_lstsqr( x0, y0)
x1= x0
y1= A1*x1 + B1
plt.plot(x1, y1, "blue")

ftext = 'y =  {:.3f} + {:.3f}x'.format(B1, A1)
plt.figtext(.15,.8, ftext, fontsize=11, ha='left')
plt.figtext(0.6,.2, "Red", fontsize=11, ha='left')
plt.ylabel('Landsat-8 OLI/TIRS')
plt.xlabel('Sentinel-2 MSI')