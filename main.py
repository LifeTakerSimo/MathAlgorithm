from logging.config import listen
import math
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


def Sum(L,k,n): #sum of the firt n element of the column L[K] (L is a list of lists)
    sumCol=0
    for i in range(0,n):
        sumCol=sumCol + L[i][k]
    return sumCol

#Initialisation
N=100 #number of patients
Pk=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.75] #probability of each treatement
K=len(Pk) #number or treatement used
Xn=[] #table of Xt
Tn=[] #table of treatment given to each patient
Nkn=K*[0] #value of Nkn at n
NknS2=[] 
NknS3=[] 
Ykn= [[0 for i in range(K)] for i in range (N)] 
"""
#Treatment of strat 1 : 
for i in range (1,N+1):
    Tnn=Stats.randint.rvs(1,K+1)  #Uniform law
    Tn.append(Tnn)
    Xt=np.random.binomial(1,Pk[Tnn-1])  #Bernoulli law
    Xn.append(Xt)  #list of efficiency{0,1} 
    for j in range (1,K+1):
        Nkn[j-1]+= np.random.binomial(1,Pk[j-1]==Pk[Tnn-1])  #number of use of all treatments on n
TE=[] #efficiency of all treatment after use 
Use=numberOfUse(Tn)
for i in range(N):
    TE.append(Xn[i]*Tn[i])
#Graphe of Strat 1 
for i in Use.keys():
    if (not(i in Eff)):
        Eff[i]=0
    ratio.append(round(Eff[i]/Use[i],2))
plt.bar(list(Eff.keys()),ratio,0.5,color='blue') #add numbers from 1 / 10 
plt.title("Graphe de l'efficacité par rapport à l'utilisation de chaque traitement",fontsize=15)
plt.ylabel('Ratio')
plt.xlabel('Traitement')
plt.grid()
plt.show()
Ex=np.mean(Xn)
print(ratio)
#Treatment of strat 2 : 
numberOfMax=[0 for k in range(K)]
PPkn=[0 for i in range (K)]
PknS2=[[0 for i in range(K)] for i in range (N)] 
for i in range (1,N+1):
    if(i<K+1):  
        Tnn=i  
        Tn.append(Tnn) 
        Xt=np.random.binomial(1,Pk[i-1])  #Bernoulli law
        Xn.append(Xt)  #list of efficiency{0,1}
    else:
        Tnn=Stats.randint.rvs(1,K+1)  #Uniform law
        Tn.append(Tnn)
        Xt=np.random.binomial(1,Pk[Tnn-1])  #Bernoulli law
        Xn.append(Xt)  #list of efficiency{0,1}
    for j in range (1,K+1):
        if(j==Tnn):
            PPkn[j-1]+= np.random.binomial(1,Pk[j-1]==Pk[Tnn-1])
    NknS2.append(PPkn.copy())
for i in range (1,N+1):
    for j in range (1,K+1):
        if(j==Tn[i-1]):
            Ykn[i-1][j-1]=Xn[i-1]
for i in range (K+1,N+1):
    for j in range (1,K+1):
        sum=Sum(Ykn,j-1,i-1)
        PknS2[i-1][j-1]=round(sum / NknS2[i-1][j-1],3)
#Graphe of strat 2
for i in range (K+1,N+1):
    for j in range(1,K+1):
        if max(PknS2[i-1])==PknS2[i-1][j-1]:
            numberOfMax[j-1]+=1
plt.bar([i for i in range(1,11)],numberOfMax,0.5) 
plt.title("",fontsize=15)
plt.ylabel('Nombre de fois ou Pkn est maximal')
plt.xlabel('Traitement')
plt.grid()
plt.show()
"""

#Treatment of strat 3 : 
 #calcul de P(K,n )

PPkn=[0 for i in range (K)]
PknS3=[[0 for i in range(K)] for i in range (N)] 
Allintervals=[[[0,0] for i in range(K)] for i in range (N)] 

for i in range (1,N+1):
    if(i<K+1):  
        Tnn=i  
        Tn.append(Tnn) 
        Xt=np.random.binomial(1,Pk[i-1])  #Bernoulli law
        Xn.append(Xt)  #list of efficiency{0,1}
    else:
        Tnn=Stats.randint.rvs(1,K+1)  #Uniform law
        Tn.append(Tnn)
        Xt=np.random.binomial(1,Pk[Tnn-1])  #Bernoulli law
        Xn.append(Xt)  #list of efficiency{0,1}
    for j in range (1,K+1):
        if(j==Tnn):
            PPkn[j-1]+= np.random.binomial(1,Pk[j-1]==Pk[Tnn-1])
    NknS3.append(PPkn.copy())


for i in range (1,N+1):
    for j in range (1,K+1):
        if(j==Tn[i-1]):
            Ykn[i-1][j-1]=Xn[i-1]

for i in range (K+1,N+1):
    for j in range (1,K+1):
        sum=Sum(Ykn,j-1,i-1)
        PknS3[i-1][j-1]=round(sum / NknS3[i-1][j-1],3)

#calculating the interval elements
def Beta(k,n):
    return(math.sqrt(2*(math.log(n))/NknS3[n-1][k-1]))

#print(PknS3)
interval=[]
supinterval=[[0 for i in range(K)] for i in range (N)] 
for i in range (K+1,N+1):
    for j in range (1,K+1):
        beta=Beta(j,i)
        inf=round(PknS3[i-1][j-1]-beta,3)
        interval.append(inf)
        sup=round(PknS3[i-1][j-1]+beta,3)
        interval.append(sup)
        supinterval[i-1][j-1]=sup
        Allintervals[i-1][j-1][0]=inf     
        Allintervals[i-1][j-1][1]=sup

#print(supinterval)
kmaxlist=[0 for i in range (N)]
for i in range (K+1,N+1):
        kmax=supinterval[i-1].index(max(supinterval[i-1]))+1
        kmaxlist[i-1]=kmax
        
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
for i in range(K+1,N+1):
    for j in range(1,K+1):
        if(j==kmaxlist[i-1]):
            xline = [i,i]
            yline=[j,j]
            zline = [Allintervals[i-1][j-1][0],Allintervals[i-1][j-1][1]]
            ax.plot3D(xline, yline, zline, 'gray')
plt.show()
    
