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

from scipy import stats as Stats
import numpy as np
from matplotlib import pyplot as plt


# Count the number of use of each element 
def numberOfUse(L):
# define empty dictionary
    occurrences = {}
# Checking the element from sample list present as key in dictionary
# if yes than increment by 1 or create new key with value 1
    for i in L:
        if i in occurrences:
            occurrences[i] += 1
        else:
            occurrences[i] = 1
# Printing dictionary
    return(occurrences)
# Printing all element with its count of Occurrence
    #for key,value in occurrences.items():
       # print("The Occurrence of {0} in the list is: {1}".format(key, value))

#Most used element in a list        
def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return num


#Stratégie 1:
#Initialisation
N=20 #number of patients
Pk=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.75] #probability of each treatement
K=len(Pk) #number or treatement used
Xt=[] #table of Xn
Tpn=[]
Nkn=K*[0] #value of Nkn at n
#Treatment of strat 1 :
for i in range (1,N+1):
    Tn=Stats.randint.rvs(1,K+1)  #Uniform law
    Tpn.append(Tn)
    Xn=np.random.binomial(1,Pk[Tn-1])  #Bernoulli law
    Xt.append(Xn)  #list of efficiency{0,1} 
    for j in range (1,K+1):
        Nkn[j-1]+= np.random.binomial(1,Pk[j-1]==Pk[Tn-1])  #number of use of all treatments on n
TE=[] #efficiency of all treatment after use 
<<<<<<< HEAD
Use=numberOfUse(Tpn)
Eff=numberOfUse(TE)
for i in range(N): 
        TE.append(Xt[i]*Tpn[i])
        RatioUE=Eff[i]/Use[i]
=======
Use=numberOfUse(Tnn)
for i in range(N):
    TE.append(Xt[i]*Tnn[i])
Eff=list(numberOfUse(TE).values())
Use=list(numberOfUse(Tnn).values())
ratio=[round(i / j,2) for i, j in zip(Use, Eff)]
print(ratio)
>>>>>>> fe46dc9e1396b8b2b545048a8d61499c4075d20d
Ex=np.mean(Xt)   
#print("L'esperance de cette stratégie est : ", Ex)
# graphe pour l'effcacite de chaque traitement 
#print(RatioUE)
