1.1_Modélisation : 
K nombre de traitements
Pk = probabilité que le traitement soit efficace 
N nombre de patients infected
Tn un traitement ( 0….n) injected for Xn

Tn Xn suite de variable aléatoire 
Nkn le nombre d’utilisation de traitement
Ykn nombre d’effacite de traitemnt 
P* = max pk ( on connait pas le meilleur traitemnt 
Apprentisssage par renforcement : deep learning 
E( somme de Xn ) : modelisation numerique pour visualiser l’efficacité 
Il faut bien expliquer les algo 

Objectif : détermination les traitemment les plus efficace ! !
	




Pour la stratégie 1 : il faut calculer la quantité 1 , avec simulations numérique à l’aide de python  

Algorithme :  Objectif trouver pk=0.9 
Etape 1 
K=10  -----  N = 1000 
Pk={0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.7,0.8,0.9,0.48} 
Etape 2 :les lois 
Tn = Uniforme ([1,10])  (traitement Tn sur le patient  n ) 
Xn  = Bernoulli (Pk)  => efficacité du traitement Tn sur le patient n  => {0,1} 
Nkn =  nombre d’utilisation du traitement jusqu’à le patient n => Binomiale(n,Pk) => somme de 1 
Somme de NkN(k) =1000 (à vérifier )
Etape 3 : Calcule Théorique 
Il faut maximser E[somme de Xn] 
E(x)  = somme i p(X=i) => E(somme de Xn) = N * E(Xi) = N * (somme j P(Xi=j))
 Alors la quantité (1) dépend de la probabilité du traitement et le nombre N
Etape 4 : 
Initialisation : voir etape 
Boucle jusqu’à 1000= N 
On choisit un traitement T selon loi uniforme ( le choix sera stocke dans le retour Tk) 
Nkn = 0 ;
On applique Tn sur le patient  n 
On déduit Xn 
Calcule de Nkn 
	Nkn / n => p
	esperance




Etape 5 
Pk tableau 
  


10 perso pk =0.5   
5 / 10 =>0. 5 


