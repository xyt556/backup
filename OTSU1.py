import matplotlib.pyplot as plt
from skimage import data
try:
    from skimage import filters
except ImportError:
    from skimage import filter as filters
from skimage import exposure

#camera = data.camera()
camera1 = data.imread('LC8IBI.jpg', True)
val = filters.threshold_otsu(camera1)

hist, bins_center = exposure.histogram(camera1)

plt.figure(figsize=(9, 4))
plt.subplot(131)
plt.imshow(camera1, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.subplot(132)
plt.imshow(camera1 < val, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.subplot(133)
plt.plot(bins_center, hist, lw=2)
plt.axvline(val, color='k', ls='--')

plt.tight_layout()
plt.show()