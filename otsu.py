"""
Otsu thresholding
==================

This example illustrates automatic Otsu thresholding.
"""

import matplotlib.pyplot as plt
from skimage import data
from osgeo import gdal
import numpy as np

try:
    from skimage import filters
except ImportError:
    from skimage import filter as filters
from skimage import exposure

#camera = data.camera()
#print camera.dtype
#x = x[numpy.logical_not(numpy.isnan(x))]
'''
camera=np.fromfile("LC8__IBI.dat",dtype=float)
#camera = camera[np.logical_not(np.isnan(camera))]
'''
#camera=np.fromfile("1.tif",dtype=int)
ds=gdal.Open("1.tif")
camera= np.array(ds.GetRasterBand(1).ReadAsArray())
c_max=max(camera)
c_min=min(camera)
print c_max,c_min
'''
camera=int( (camera-c_min) / (c_max-c_min) * 255 )

#camera = camera[np.logical_not(np.isnan(camera))]

#print type(camera)


#val = filters.threshold_otsu(camera)
val=filters.threshold_otsu(camera)

print val
hist, bins_center = exposure.histogram(camera)



plt.figure(figsize=(9, 4))
plt.subplot(131)
plt.imshow(camera, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.subplot(132)
plt.imshow(camera < val, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.subplot(133)


plt.plot(bins_center, hist, lw=2)
plt.axvline(val, color='k', ls='--')

plt.tight_layout()
plt.show()
'''