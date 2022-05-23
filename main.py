"""
# -*- coding: utf-8 -*-
Created on Thu May  5 14:16:37 2022
@author: Asus
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
"""

from ipaddress import NetmaskValueError
from operator import index
from scipy import stats as Stats
import numpy as np
from matplotlib import pyplot as plt

#Stratégie 1:
#Initialisation
N=15 #number of patients
Pk=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.48] #probability of each traitement
K=len(Pk) #number or treatement used
pk=K*[0] #final probability of each treatment
Xt=[] #table of Xn
Nkn=N*[K*[0]]
LNkn=K*[0] #value of Nkn on n
for i in range (1,N+1):
    Tn=Stats.randint.rvs(1,K+1)  #Uniform law
    print("Tn =",Tn)
    Xn=np.random.binomial(1,Pk[Tn-1])  #Bernoulli law
    Xt.append(Xn)  #list of efficiency{0,1} 
    for j in range (1,K+1):

        LNkn[j-1]+= np.random.binomial(1,Pk[j-1]==Pk[Tn-1])  #number of use of all treatments on n
   
    print("Nkn=",LNkn)

for j in range(1,K+1):
    pk[j-1]=LNkn[j-1]/N

Ex=np.mean(Xt)

print(Ex)



    


