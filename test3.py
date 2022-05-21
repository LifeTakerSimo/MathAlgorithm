# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:16:37 2022

@author: Asus
"""
import numpy as np
from matplotlib import pyplot as plt
# pour visualiser la loi de bernoulli
from scipy.stats import bernoulli
data_bernoulli = bernoulli.rvs(size=1000,p=1)
x=np.linspace(1, 1000, 1000)
plt.xlabel('number',color='red')
plt.ylabel('Bernoulli',color='red')
print(data_bernoulli)
plt.plot([x],[data_bernoulli])
plt.grid(True)
plt.show()
plt.text()
plt.title("Bernoulli Strategie 1 ")
#ax = sb.displot(data_bernoulli,kde=True,color='red',hist_kws={"linewidth": 25, 'alpha': 1})
#ax.set(xlabel='Loi de bernoulli' , ylabel='Frequency')