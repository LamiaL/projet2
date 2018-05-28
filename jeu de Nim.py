
# coding: utf-8

# In[ ]:


#les joueurs
user_input = input('le nom du premier joueure : ')
joueur1=user_input
user_input = input('le nom du deuxième joueure : ')
joueur2=user_input#demande du l'utilisateur les des joueures
import pickle
infile= open ("pickle.txt","rb")
new_liste=pickle.load (infile)
print ('la liste des joueurs et leurs score :')
print (new_liste)
infile.close()#afficher la liste des joueure déja jouent et leus scores

#lancement du jeu
def etat_du_jeu(nombretas,pierre):    #fonction pour afficher l'état du jeu
 k=0
 for nombretas in range(0, nombretas):
  print (k+1 ,'|' ,end='') 
  y=pierre[k]
  for y in range(0, y):
    print ('*' , end='')
  print ('|', pierre[k])
  k=k+1 
somme = 0    #somme le nombre des pierre dans tous les tas
i=0
nombre_pierre=[]
import random            
nombre_tas=(random.randint(3,7))
for nombre_tas in range(0, nombre_tas-1):
 p=(random.randint(5,23))
 nombre_pierre.append(p)
 i=i+1
 somme = somme + p 
somme = somme - p
print ('____________________________________________________________________')
print ('l\'état du jeu est:')
etat_du_jeu(nombre_tas,nombre_pierre)
print ('____________________________________________________________________')
#tour du jeu
j = joueur1
nbcoup1 = 0
nbcoup2 = 0
score = 0
while somme not in [0, 1]: #si il reste un seule pierre ou 0  alors fin du jeu 
 print ('le tour du' , j)
 user_input = input('le  num de tas ')
 tas_num=int(user_input)
 if tas_num>nombre_tas:
    erreur=1    
    print ('erreur')
 user_input = input('le nombre des pierres ')
 pierre_num=int(user_input)
 if nombre_pierre[tas_num-1]<pierre_num:
    print ('erreure')
 else:
  nombre_pierre[tas_num-1]=nombre_pierre[tas_num-1]-pierre_num
  print ('___________________________________________________________________')
  print ('l\'état du jeu est:')
  etat_du_jeu(nombre_tas,nombre_pierre)
  print ('___________________________________________________________________')
  somme = somme - pierre_num
 if j is joueur1:
    j= joueur2    #le tour du l'autre joueur
    nbcoup1 = nbcoup1 + 1 #NbCoup pour le joueur 1
 else: 
   j=joueur1
   nbcoup2 = nbcoup2 + 1  #NbCoup pour le joueur 2
    
   
if j is joueur1:
 if somme is 1 : 
  j=joueur2
 nbcoup2 = nbcoup2 +1
 for nbcoup2 in range(1,nbcoup2):
    score = score + nbcoup2*(10**nbcoup2) #calculer le score si le joueure 2 gagne
else:
 if somme is 1:
  j=joueur1
 nbcoup1 = nbcoup1 +1
 for nbcoup1 in range(1,nbcoup1):
    score = score + nbcoup1*(10**nbcoup1 )  #calculer le score si le joueure 2 gagne
    

print ('-----------------------------------------------------------------------')
print ('***********************************************************************')
print ('the winer is ',j)
print ('le score est',score) #pour afficher le joueur qui gange et on score
print ('***********************************************************************')
print ('-----------------------------------------------------------------------')
scores = []
scores.append((j,score))
print (scores)
outfile = open("pickle.txt","wb")
pickle.dump(scores,outfile)
outfile.close() #pour enregistre le nom du joueure qui gagne et son score
#fin du jeu

