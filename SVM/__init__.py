Y = [0]*20 +[1]*20
# 绘图  前二十  后二十
import numpy as np
import pylab as pl
from sklearn import svm
X = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
