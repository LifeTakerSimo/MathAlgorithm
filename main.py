from scipy import stats as stats
import numpy as np
from matplotlib import pyplot as plt

def initialisation():
    global N,Pk,K,Xn,Tn,Nkn,Nkn,Ykn
    N=1000 #number of patients
    Pk=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.75] #probability of each treatement
    K=len(Pk) #number or treatement used
    Xn=[] #table of Xt
    Tn=[] #table of treatment given to each patient
    Nkn=K*[0] #value of Nkn at n
    Ykn= [[0 for i in range(K)] for i in range (N)] 
# Count the number of use of each element 
def numberOfUse(L):
    occurrences = {}
    for i in L:
        if i==0:
            continue
        else:
            if i in occurrences:
                occurrences[i] += 1
            else:
                occurrences[i] = 1
    return(occurrences)

def Sum(L,k,n): #sum of the firt n element of the column L[K] (L is a list of lists)
    sumCol=0
    for i in range(0,n):
        sumCol=sumCol + L[i][k]
    return sumCol

def Strategie1():
    for i in range (1,N+1):
        Tnn=stats.randint.rvs(1,K+1)  #Uniform law
        Tn.append(Tnn)
        Xt=np.random.binomial(1,Pk[Tnn-1])  #Bernoulli law
        Xn.append(Xt)  #list of efficiency{0,1} 
        for j in range (1,K+1):
            Nkn[j-1]+= np.random.binomial(1,Pk[j-1]==Pk[Tnn-1])  #number of use of all treatments on n
    TE=[] #efficiency of all treatment after use 
    for i in range(0,N):
        TE.append(Xn[i]*Tn[i])
        
    Use=numberOfUse(Tn)
    Eff=numberOfUse(TE)
    ratio=[]
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

def Strategie2(): 
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
            Tnn=stats.randint.rvs(1,K+1)  #Uniform law
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


while(False):
    print("Entre le numéro de la stratégie à choisir:\n1- Statégie 1\n2- Stratégie 2\n3- Stratégie 3\n4- Stratégie4\n")
    choice=input()
    if(choice=="1"):
        initialisation()
        Strategie1()
    if(choice=="2"):
        initialisation()
        Strategie2()
