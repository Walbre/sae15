
import matplotlib.pyplot as plt

from traiter import data_handler

myData = data_handler("../data.csv")


fig, ax = plt.subplots(2, 2)

#################### graphe en 2,1 (comparaison swap et mem)

y1 = myData.get_column(3)

y2 = myData.get_column(6)

for i in range(len(y1)):
    y1[i] = y1[i]/10**6
    y2[i] = y2[i]/10**6

x = [i for i in range(1, len(y1) + 1)]


    
ax[1, 0].plot(x, y1, 'r-', label="Memoire disponible")

ax[1, 0].plot(x, y2, 'b-', label="Swap disponible")


ax[1, 0].set_title("Evolution de la mémoire libre")
ax[1, 0].set_xlabel("Temps (min)")
ax[1, 0].set_ylabel("Memoire (Gb)")

ax[1, 0].legend()


############### graphe en 1, 1 (pourcentage d'utilisation de la mémoire)


y_mem = myData.get_column(3) # memoire disponible

x = [i for i in range(len(y_mem))]

mem_totale = myData.get_column(1)[0] # memoire totale

ligne_nulle = [0 for _ in range(len(y_mem))]

pourcentage = [round((mem_totale - y_mem[i]) / mem_totale, 5)*100 for i in range(len(y_mem))] # pourcentage de memoire utilisee



ax[0, 0].fill_between(x, ligne_nulle, pourcentage, color="#d487eba0")

ax[0, 0].set_title("Pourcentage de mémoire \n utilisée")
ax[0, 0].set_xlabel("Temps (min)")
ax[0, 0].set_ylabel("Mémoire utilisée (%)")




######################### graph en 1,2 (pourcentage d'utilisation de la meme Swap)

y_mem = myData.get_column(6) # memoire swap disponible

x = [i for i in range(len(y_mem))]

mem_totale = myData.get_column(5)[0] # memoire swap totale

ligne_nulle = [0 for _ in range(len(y_mem))]

pourcentage = [round((mem_totale - y_mem[i]) / mem_totale, 5)*100 for i in range(len(y_mem))] # pourcentage de memoire utilisee



ax[0, 1].fill_between(x, ligne_nulle, pourcentage, color="#64cfd1a0")

ax[0, 1].set_title("Pourcentage de mémoire \n Swap utilisée")
ax[0, 1].set_xlabel("Temps (min)")
ax[0, 1].set_ylabel("Mémoire Swap utilisée (%)")




################### camembert memoire moyenne et libre

mem_total = myData.get_column(1)[0]

average_mem_free = (myData.average(2) / mem_total) * 100

average_mem_available = (myData.average(3) / mem_total) * 100


values = [average_mem_free, average_mem_available - average_mem_free, 100 - average_mem_available]
labels = ["Libre", "Utilisable", "Utilisée"]

ax[1, 1].pie(values, labels=labels, autopct='%1.1f%%')


############## affichage des valeurs
fig.supxlabel(f"Mémoire moyenne utilisée : {round(myData.average(1)/10**6 - myData.average(3)/10**6, 3)}/{round(myData.average(1)/10**6, 3)}Gb")

ax[1, 0].legend()
plt.tight_layout()
plt.show()