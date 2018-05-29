
# coding: utf-8

# In[ ]:


#les données
user_input = input('le premier nombre : ')
a=int(user_input)
user_input = input('le deuxième nombre : ')
b=int(user_input)

ens = [] #l'ensemble
for i in range (0,b-a+1) :
    ens.append(a+i) 
#chercher les carrés parfaits dans l'ensemble et leurs nombres
import math
nbp =0 
print ("les carrés parfaits sont ")
for i in range (0,b-a+1) : 
    if math.sqrt(ens[i]).is_integer():
      nbp = nbp + 1 
      
      print (ens[i])
print( "il y'a ", end='')
print (nbp , end='' )
print (" carrés parfait dans ce intervalle")

for i in range (0,b-a+1) : 
 for j in range (1,b-a+1) :
   if i !=j :
    if math.sqrt(ens[i]*ens[j]).is_integer():
      nbp = nbp + 1 

