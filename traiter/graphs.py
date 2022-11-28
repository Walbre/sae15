
import matplotlib.pyplot as plt

from traiter import data_handler

myData = data_handler("../data.csv")


fig, ax = plt.subplots(2, 2)

#################### graphe en 1,2 (comparaison swap et mem)

y1 = myData.get_column(3)

y2 = myData.get_column(6)

x = [i for i in range(1, len(y1))]



for i in range(1, len(x) - 1): # jusqu'a len()-1 pour que la derniere ligne serve au titre
    ax[1, 0].plot([x[i-1], x[i]], [y1[i-1]/ 10**6, y1[i]/ 10**6], 'r-')
    
ax[1, 0].plot([x[-2], x[-1]], [y1[-2]/ 10**6, y1[-1]/ 10**6], 'r-', label="Memoire disponible") # ajouter le titre


for i in range(1, len(x) - 1):
    ax[1, 0].plot([x[i-1], x[i]], [y2[i-1]/ 10**6, y2[i]/ 10**6], 'b-')
    
ax[1, 0].plot([x[-2], x[-1]], [y2[-2]/10**6, y2[-1]/10**6], 'b-', label="Swap disponible") # ajouter le titre


ax[1, 0].set_title("Evolution de la mémoire libre")
ax[1, 0].set_xlabel("Temps (min)")
ax[1, 0].set_ylabel("Memoire (Gb)")


############### graphe en 1, 1 (pourcentage d'utilisation de la mémoire)


y_mem = myData.get_column(3) # memoire disponible

x = [i for i in range(len(y_mem))]

mem_totale = myData.get_column(1)[0] # memoire totale

ligne_nulle = [0 for _ in range(len(y_mem))]

pourcentage = [round((mem_totale - y_mem[i]) / mem_totale, 5) for i in range(len(y_mem))] # pourcentage de memoire utilisee

for i in range(1, len(x)):
    ax[0, 0].plot([x[i-1], x[i]], [pourcentage[i-1], pourcentage[i]], '-', color="#b171c4")

ax[0, 0].fill_between(x, ligne_nulle, pourcentage, color="#d487eba0")

ax[0, 0].set_title("Pourcentage de mémoire utilisée")
ax[0, 0].set_xlabel("Temps (min)")
ax[0, 0].set_ylabel("Mémoire utilisée (%)")




    

############## affichage des valeurs
fig.supxlabel(f"Mémoire moyenne utilisée : {round(myData.average(3)/10**6, 3)}/{round(myData.average(1)/10**6, 3)}Gb")

plt.legend(loc='upper center')
plt.tight_layout()
plt.show()