# -*- coding: utf-8 -*-
import matplotlib  #导入matplotlib库
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
#画曲线图
fig = plt.figure()
def f(x1, c):
     m1 = sin(2*pi*x1)
     m2 = exp(-c*x1)
     return multiply(m1, m2)
x = linspace(0,4,100)
sigma = 0.5
plt.plot(x, f(x, sigma), 'r', linewidth=2)
plt.xlabel(r'$\rm{time}  \  t$', fontsize=16)
plt.ylabel(r'$\rm{Amplitude} \ f(x)$', fontsize=16)
plt.title(r'$f(x) \ \rm{is \ damping  \ with} \ x$', fontsize=16)
plt.text(2.0, 0.5, r'$f(x) = \rm{sin}(2 \pi  x^2) e^{\sigma x}$', fontsize=20)
plt.savefig('latex.png', dpi=75)
plt.show()

#画柱状图
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, '%s' % float(height))

plt.xlabel(u'性别')
plt.ylabel(u'人数')
plt.title(u"性别比例分析")
plt.xticks((0,1),(u'男',u'女'))
rect = plt.bar(left = (0,1),height = (1,0.5),width = 0.35,align="center")

plt.legend((rect,),(u"图例",))
autolabel(rect)
plt.show()

#画散列点
mu_vec1 = np.array([0,0])
cov_mat1 = np.array([[2,0],[0,2]])

x1_samples = np.random.multivariate_normal(mu_vec1, cov_mat1, 100)
x2_samples = np.random.multivariate_normal(mu_vec1+0.2, cov_mat1+0.2, 100)
x3_samples = np.random.multivariate_normal(mu_vec1+0.4, cov_mat1+0.4, 100)

# x1_samples.shape -> (100, 2), 100 rows, 2 columns

plt.figure(figsize=(8,6))

plt.scatter(x1_samples[:,0], x1_samples[:,1], marker='x',
            color='blue', alpha=0.7, label='x1 samples')
plt.scatter(x2_samples[:,0], x1_samples[:,1], marker='o',
            color='green', alpha=0.7, label='x2 samples')
plt.scatter(x3_samples[:,0], x1_samples[:,1], marker='^',
            color='red', alpha=0.7, label='x3 samples')
plt.title('Basic scatter plot')
plt.ylabel('variable X')
plt.xlabel('Variable Y')
plt.legend(loc='upper right')

plt.show()