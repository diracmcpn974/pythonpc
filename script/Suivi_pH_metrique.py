# -*- coding: utf-8 -*-
"""
Suivi pH-metrique d'un titrage

Titrage d'une solution aqueuse d'acide ethanoique par une solution aqueuse
d'hydroxyde de sodium.
"""

#Importation des bibliothèques
import matplotlib.pyplot as plt
import numpy as np
#from scipy import stats

#Partie du programme a completer avec les valeurs de volume de solution titrante verse et le pH correspondant
Vb = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,12.2,12.4,12.6,12.8,13,13.2,13.4,
13.6,13.8,14,14.2,14.4,14.6,14.8,15,16,17,18,19,20,21,22,23,24,25])
pH = np.array([3.21,3.60,3.88,4.07,4.24,4.38,4.51,4.64,4.78,4.93,5.11,5.28,5.60,5.69,5.78,
5.95,6.03,6.28,6.75,7.08,9.32,10.26,10.68,10.83,10.94,11.1,11.17,
11.29,11.47,11.60,11.70,11.83,11.90,11.95,12.00,12.02,12.08,12.10])
#derpH=derivee(Vb,pH)
def derivee(x,y):
    dery=[]
    for i in range (len(x)-1):
        deryi=(y[i+1]-y[i])/(x[i+1]-x[i])
        dery.append(deryi)
    return dery

derpH=derivee(Vb,pH)
#print(derpH) #Affichage facultatif

#Suppression de la derniere valeur du tableau a cause de l'affichage de la courbe de la derivee
Vb = np.delete(Vb,-1)
pH = np.delete(pH,-1)

plt.figure(figsize=(10,10))
plt.subplot(2,1,1)
plt.plot(Vb,pH,"r+-", label=r'$pH$')
plt.xlabel(r'$Vb \ (mL)$')
plt.ylabel(r'$pH$')
plt.grid()
plt.title("Titrage de l'acide ethanoique par la soude")
plt.legend()
plt.subplot(2,1,2)
plt.plot(Vb,derpH,"b+-",label=r'$Derivee$')
plt.xlabel(r'$Vb \ (mL)$')
plt.ylabel(r'$Derivee \ (mL^{-1})$')
plt.grid()
plt.title("Determination du volume equivalent")
plt.legend()
plt.show()

#Determination du volume equivalent
Vbe = Vb[(derpH.index(max(derpH)))]
print ("Vbe=",Vbe,"mL")

#Evolution des quantites de matieres des reactifs et prduits dans le vase reactionnel
cb = 0.1 #Concentration de la solution titrante d'hydroxyde de sodium
na=np.array([])
nb=np.array([])
nc=np.array([])
for i in range (len(Vb)):
    if Vb[i]<=Vbe:
        nai = cb*Vbe-cb*Vb[i] #Qte de matiere d'acide ethanoique en mmol
        nbi = 0        #Qte de matiere des ions hydroxyde en mmol
        nci = cb*Vb[i] #Qte de matiere des ions éthanoate en mmol
        na = np.append(na,nai)
        nb = np.append(nb,nbi)
        nc = np.append(nc,nci)
    else:
        nai = 0 #Qte de matiere d'acide ethanoique en mmol
        nbi = cb*(Vb[i]-Vbe) #Qte de matiere des ions hydroxyde en mmol
        nci = cb*Vbe         #Qte de matiere des ions ethanoate en mmol
        na = np.append(na,nai)
        nb = np.append(nb,nbi)
        nc = np.append(nc,nci)
#print (na) #Affichage facultatif
#print (nb) #Affichage facultatif
#print (nc) #Affichage facultatif

#Trace de la courbe
plt.figure(figsize=(12,10))
plt.plot(Vb,na,"b+-",label="Acide ethanoique")
plt.plot(Vb,nb,"g+-",label="Ions hydroxyde")
plt.plot(Vb,nc,"r+-",label="Ions ethanoate")
plt.xlabel("Volume de reactif titrant (mL)")
plt.ylabel("Quantite de matiere (mmol)")
plt.title("Etude des quantites de matiere des especes chimiques presentes dans le vase reactionnel")
plt.legend()
plt.grid()
plt.show()





