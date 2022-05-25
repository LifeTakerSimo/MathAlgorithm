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
        if i==0:
            continue
        else:
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
N=1000 #number of patients
Pk=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.75] #probability of each treatement
K=len(Pk) #number or treatement used
Xt=[] #table of Xn
Tnn=[] #table of treatment given to each patient
Nkn=K*[0] #value of Nkn at n
Ykn= [[0 for i in range(K)] for i in range (N)] 

#Treatment of strat 1 : 
for i in range (1,N+1):
    Tn=Stats.randint.rvs(1,K+1)  #Uniform law
    Tnn.append(Tn)
    Xn=np.random.binomial(1,Pk[Tn-1])  #Bernoulli law
    Xt.append(Xn)  #list of efficiency{0,1} 
    for j in range (1,K+1):
        Nkn[j-1]+= np.random.binomial(1,Pk[j-1]==Pk[Tn-1])  #number of use of all treatments on n
TE=[] #efficiency of all treatment after use 
Use=numberOfUse(Tnn)
for i in range(N):
    TE.append(Xt[i]*Tnn[i])
Eff=numberOfUse(TE)
Use=numberOfUse(Tnn)
ratio=[]
for i in Use.keys():
    if (not(i in Eff)):
        Eff[i]=0
    ratio.append(round(Eff[i]/Use[i],2))
plt.bar(list(Eff.keys()),ratio,0.5,color='blue')
plt.title("Graphe de l'efficacité par rapport à l'utilisation de chaque traitement",fontsize=15)
plt.ylabel('Ratio')
plt.xlabel('Traitement')
plt.grid
plt.show()
Ex=np.mean(Xt)
print(ratio)
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
            Ykn[i-1][j-1]=Xt[i-1]
            #print(Ykn)
print(len(Ykn))
print(len(Ykn[0]))
print(Ykn)            
#print(Tnn)
#print(Xt)
#print(Ykn)
"""
