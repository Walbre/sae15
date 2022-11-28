
import matplotlib.pyplot as plt

from traiter import data_handler

myData = data_handler("../data.csv")

y1 = myData.get_column(3)

y2 = myData.get_column(6)

x = [i for i in range(1, len(y1))]

fig, ax = plt.subplots()



for i in range(1, len(x) - 1): # jusqu'a len()-1 pour que la derniere ligne serve au titre
    ax.plot([x[i-1], x[i]], [y1[i-1]/ 10**6, y1[i]/ 10**6], 'r-')
    
ax.plot([x[-2], x[-1]], [y1[-2]/ 10**6, y1[-1]/ 10**6], 'r-', label="Memoire libre") # ajouter le titre


for i in range(1, len(x) - 1):
    ax.plot([x[i-1], x[i]], [y2[i-1]/ 10**6, y2[i]/ 10**6], 'b-')
    
ax.plot([x[-2], x[-1]], [y2[-2]/10**6, y2[-1]/10**6], 'b-', label="Swap libre") # ajouter le titre


ax.set_title("Evolution de la mémoire libre")
ax.set_xlabel("Temps (60s)")
ax.set_ylabel("Memoire (Gb)")


    

print(f"Moyenne de mémoire utilisee : {myData.average(3)}/{myData.average(1)} ({myData.get_name(3)}/{myData.get_name(1)})")

fig.supxlabel(f"Mémoire moyenne utilisée : {round(myData.average(3)/10**6, 3)}/{round(myData.average(1)/10**6, 3)}Gb")

plt.legend(loc='upper center')
plt.tight_layout()
plt.show()