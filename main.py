import math
from scipy import stats as Stats
import numpy as np
from matplotlib import pyplot as plt

def initialisation():
    global N,Pk,K,Xn,Tn,Nkn,Ykn,NknS2,NknS3,NknS4,PPkn,Pkn,Allintervals
    N=100 #number of patients
    Pk=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.75] #probability of each treatement
    K=len(Pk) #number or treatement used
    Xn=[] #table of Xt
    Tn=[] #table of treatment given to each patient
    Nkn=K*[0] #value of Nkn at n
    Ykn= [[0 for i in range(K)] for i in range (N)]
    NknS2=[]
    NknS3=[]
    NknS4=[]
    Pkn=[[0 for i in range(K)] for i in range (N)] 
    PPkn=[0 for i in range (K)] 
    Allintervals=[[[0,0] for i in range(K)] for i in range (N)] 
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
        Tnn=Stats.randint.rvs(1,K+1)  #Uniform law
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
    ratio=[] #nombre d'efficacité/nombre d'utilisation
    for i in range(N):
        TE.append(Xn[i]*Tn[i])
    #Graphe of Strat 1 
    for i in Use.keys():
        if (not(i in Eff)):
            Eff[i]=0
        ratio.append(round(Eff[i]/Use[i],2))
    plt.bar(list(Eff.keys()),ratio,0.5,color='blue') #add numbers from 1 / 10 
    plt.title("Graphe de l'efficacité par rapport à l'utilisation de chaque traitement",fontsize=15)
    plt.ylabel("Ratio = Efficacité / Utilisation")
    plt.xlabel('Traitement')
    plt.grid()
    plt.show()
    Ex=np.mean(Xn)

def Strategie2(): 
    numberOfMax=[0 for k in range(K)]
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
            Pkn[i-1][j-1]=round(sum / NknS2[i-1][j-1],3)
    #Graphe of strat 2
    for i in range (K+1,N+1):
        for j in range(1,K+1):
            if max(Pkn[i-1])==Pkn[i-1][j-1]:
                numberOfMax[j-1]+=1
    plt.bar([i for i in range(1,11)],numberOfMax,0.5) 
    plt.title("",fontsize=15)
    plt.ylabel('Nombre de fois ou Pkn est maximal')
    plt.xlabel('Traitement')
    plt.grid()
    plt.show()
    
def Strategie3():

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
            Pkn[i-1][j-1]=round(sum / NknS3[i-1][j-1],3)
    
    #calculating the interval elements
    def Beta(k,n):
        return(math.sqrt(2*(math.log(n))/NknS3[n-1][k-1]))
    
    #print(Pkn)
    interval=[]
    supinterval=[[0 for i in range(K)] for i in range (N)] 
    for i in range (K+1,N+1):
        for j in range (1,K+1):
            beta=Beta(j,i)
            inf=round(Pkn[i-1][j-1]-beta,3)
            interval.append(inf)
            sup=round(Pkn[i-1][j-1]+beta,3)
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
    color=['blue','red','yellow','grey','purple','green','magenta','brown','black','orange']
    # Data for a three-dimensional line
    for i in range(K+1,N+1):
        for j in range(1,K+1):
            if(j==kmaxlist[i-1]):
                xline = [i,i]
                yline=[j,j]
                zline = [Allintervals[i-1][j-1][0],Allintervals[i-1][j-1][1]]
                Top=[i-0.5,i+0.5]
                ax.plot3D(xline, yline, zline, color[j-1])
                ax.plot3D(Top, yline, zline, color[j-1])
    ax.set_xlabel('N')
    ax.set_ylabel('Traitement')
    ax.set_zlabel('Intervalle de confiance')
    ax.set_title('Stratégie 3')
    plt.show()
    
def Strategie4():
    
# calcule de somme de Yk,i 
    for i in range (1,N+1):
        Tnn=Stats.randint.rvs(1,K+1)  #Uniform law
        Tn.append(Tnn)
        Xt=np.random.binomial(1,Pk[Tnn-1])  #Bernoulli law
        Xn.append(Xt)  #list of efficiency{0,1}
        
        for j in range (1,K+1):
            if(j==Tnn):
                PPkn[j-1]+= np.random.binomial(1,Pk[j-1]==Pk[Tnn-1])
        NknS4.append(PPkn.copy())
    for i in range (1,N+1):
        for j in range (1,K+1):
            if(j==Tn[i-1]):
                Ykn[i-1][j-1]=Xn[i-1]
    for j in range(1,K+1):
                Pkn[0][j-1]=Stats.beta.rvs(a=1, b=1) #law of Beta 
    for i in range(2,N+1):
        for j in range(1,K+1):
                a=1+Sum(Ykn,j-1,i-1)
                b=1+NknS4[i-1][j-1]-Sum(Ykn,j-1,i-1)
                Pkn[i-1][j-1]=Stats.beta.rvs(a,b)
    PknMax=[0 for i in range(N)]
    for i in range(1,N+1):
        PknMax[i-1]=Pkn[i-1].index(max(Pkn[i-1]))+1
    ax = plt.axes(projection='3d')
    color=['red','orange','yellow','green','blue','purple','pink','lime','gray','brown']
    # Data for a three-dimensional line
    for i in range(1,N+1):
        for j in range(1,K+1):
            if(j==PknMax[i-1]):
                xline = [i,i]
                yline=[j,j]
                zline = [0,Pkn[i-1][j-1]]
                ax.plot3D(xline, yline, zline, color[j-1])
    ax.set_xlabel('Instant n')
    ax.set_ylabel('Traitement k')
    ax.set_zlabel('Pk,n')
    ax.set_title('Stratégie 4')
    plt.show()
    
# def Strategie5():
    # k=1
    # TU=[ i for i in range(0,10)]
    # TE=[]
    # print(Tn)
    # while(len(TU)!=1):
    #     for i in range(1,K+1):
    #         for j in range(0,math.floor(N/K)):
    #             Tn.append(k)
    #         k+=1
    #     for i in range(1,N+1):
    #         Xt=np.random.binomial(1,Pk[Tn[i-1]-1])  #Bernoulli law
    #         TE.append(Xt*Tn[i-1])
    #     Eff=numberOfUse(TE)
    #     for i in range(1,N+1):
    #         if(Eff[i]==min(Eff)):
    #             TU.pop(Eff[i])
while(True):
    print("Entre le numéro de la stratégie à choisir:\n1- Statégie 1\n2- Stratégie 2\n3- Stratégie 3\n4- Stratégie 4\n5- Exit\n")
    choice=input()
    if(choice=="1"):
        initialisation()
        Strategie1()
    else:
        if(choice=="2"):
            initialisation()
            Strategie2()
        else:
            if(choice=="3"):
                initialisation()
                Strategie3()
            else:
                if(choice=="4"):
                    initialisation()
                    Strategie4()
                else:
                    if(choice=="5"):
                        initialisation()
                        Strategie5()
    
