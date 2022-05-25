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



#Initialisation
N=15 #number of patients
Pk=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.75] #probability of each treatement
K=len(Pk) #number or treatement used
Xt=[] #table of Xn
Tnn=[] #table of treatment given to each patient
Nkn=K*[0] #value of Nkn at n
Ykn=K*[N*[0]]   # la grande list : [k element]  => each element contains N => [1, 2, 3, , ...10]
Yk= [ 0 for element in range(N)]
Ykn = [Yk for element in range(K)]
"""

#Treatment of strat 1 : 
for i in range (1,N+1):
    Tn=Stats.randint.rvs(1,K+1)  #Uniform law
    Tnn.append(Tn)
    Xn=np.random.binomial(1,Pk[Tn-1])  #Bernoulli law
    Xt.append(Xn)  #list of efficiency{0,1} 
    for j in range (1,K+1):
        Nkn[j-1]+= np.random.binomial(1,Pk[j-1]==Pk[Tn-1])  #number of use of all treatments on n
TE=[] #efficiency of all treatment after use 
for i in range(N):
    TE.append(Xt[i]*Tnn[i])
Eff=list(numberOfUse(TE).values())
Use=list(numberOfUse(Tnn).values())
ratio=[round(i / j,2) for i, j in zip(Use, Eff)]
print(Nkn)
Ex=np.mean(Xt)   
====
print(ratio)
print(len(ratio))
Ex=np.mean(Xt)
#print("L'esperance de cette stratégie est : ", Ex)
#graphe pour l'effcacite de chaque traitement 
#print(RatioUE)

"""
#Treatment of strat 2 : 
for i in range (1,N+1):
    if(i<K+1):    
        Tnn.append(i) 
        Xn=np.random.binomial(1,Pk[i-1])  #Bernoulli law
        Xt.append(Xn)  #list of efficiency{0,1}
        #print(Xt)
    else:
        Tn=Stats.randint.rvs(1,K+1)  #Uniform law
        Tnn.append(Tn)
        Xn=np.random.binomial(1,Pk[Tn-1])  #Bernoulli law
        Xt.append(Xn)  #list of efficiency{0,1}
for i in range (1,N+1):
    for j in range (1,K+1):
        if(j==Tnn[i-1]):
            Ykn[j-1][i-1]=Xt[i-1]
            #print(Ykn)
    print(Ykn)            
#print(Tnn)
#print(Xt)
#print(Ykn)







