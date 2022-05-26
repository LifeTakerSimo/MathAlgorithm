
L=[[i for i in range(5)] for i in range (8)] 

print(L)

def Sumn(Liste,n):
    K=len(Liste)
    sum=0
    for i in range(min(n,K)):
        sum+=Liste[i]