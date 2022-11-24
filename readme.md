# SAE 15 

## Liste des fichiers

- `data.csv`

Fichier contenant différentes informations sur la mémoir de l'ordinateur a un instant t

Il se décompose en plusieurs colonnes
```
time,MemTotal,MemFree,MemAvilable,SwapCached,SwapTotal,SwapFree
```
time étant le timestamp au moment de la capture et les autre colonnes, différentes données provenant de `/proc/meminfo`.

Le fichier `data.csv.back` est une copie de ce fichier, pour pouvoir récuperer les données en cas de mauvaise manipulation.


- `resetScript.sh`

Fichier de script permettant de vider le fichier ./data.csv en ne laissant que le nom des différentes colonnes (donc la 1<sup>ère</sup> ligne)

- `script.sh`

Fichier de script récuperant les valeurs `MemTotal, MemFree, MemAvilable, SwapCached, SwapTotal et SwapFree` du fichier `/proc/meminfo` et les ajoutant dans une nouvelle ligne du fichier `/root/Documents/sae15/data.csv` (chemin absolu necessaire pour cron).

- `varier.sh`

Fichier faisant varier la memoire utiliser par l'ordinateur. Pour celà, ce script augmente la taille d'un variable (jusqu'à atteindre 1/2 milliard de caractère).

- `traiter/traiter.py`

Fichier python servant a traiter les informations du fichier `data.csv`.


## Aquisition des données

Pour récuperer les données du fichier `data.csv` il a fallu planifier le lancement du script `script.sh` avec cron. Ansi, toute les minutes, le fichier `data.csv` s'agrandissait d'une ligne. Pendant ce temps, pour rendre les données interessantes, il a fallu lancer a plusieurs reprises le script `varier.sh` qui faisait augmenter la mémoire allouer par la machine.