
import matplotlib.pyplot as plt

from traiter import data_handler

myData = data_handler("../data.csv")

y1 = myData.get_column(3)

y2 = myData.get_column(4)

x = [i for i in range(1, len(y1))]


for i in range(1, len(x)):
    plt.plot([x[i-1], x[i]], [y1[i-1], y1[i]], 'r-')



for i in range(1, len(x)):
    plt.plot([x[i-1], x[i]], [y2[i-1], y2[i]], 'b-')
    

print(f"Moyenne de mémoire utilisee : {myData.average(3)}/{myData.average(1)} ({myData.get_name(3)}/{myData.get_name(1)})")

    

    
plt.show()