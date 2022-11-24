#!/usr/bin/python

import csv
import os
from typing import List

# changement du repertoire d'execution du fichier
directory = os.path.dirname(__file__)
print(f"Execution du fichier dans {directory}")

os.chdir(directory)

class data_handler:

    def __init__(self, filename:str, separateur=',') -> None:
        """
        Creation de la classe qui va servir aux interactions avec le fichier csv
        """
        self.separateur = separateur
        
        self.filename : str = filename
        
        self.lines : List[str] = []
        
        self.raw : str = ""
        
        with open(filename, newline='') as csvfile :
            datareader = csv.reader(csvfile, delimiter=self.separateur, quotechar='|')
            
            for line in datareader:
                # ajouter les lignes a la liste
                self.lines.append(line)
                
                # ajouter les lignes sous la frome de string dans le string
                self.raw += ",".join(line) + "\n"
        
    def get_raw_data_in_string(self) -> str:
        """
        Renvoie les donnees brutes du fichier csv en format string
        
        Returns:
            str: les donnees du fichier
        """
        return self.raw

    
    def get_data_in_list(self, first_line=False) -> List[List[str]]:
        """
        Renvoie une liste a 2 dimensions qui contient les differentes donnees en string
        
        Exemple pour le fihier csv
        a, b, c
        d, e, f
        g, h, i
        
        >> [[a, b, c], [d, e, f], [g, h, i]]
        
        Args:
            first_line bool (default to False): si first_line est a False alors la premier ligne n'est pas renvoyee

        Returns:
            List[List[str]]: la liste de liste
        """
        return self.lines[1:] if not first_line else self.line

    def average_time_diff(self) -> float:
        """
        Calcule le temps moyen entre 2 lignes du fichier csv

        Returns:
            float: Le temps moyen
        """
        
        data = self.get_data_in_list()

myData = data_handler("../data.csv")

print(myData.get_raw_data_in_string())
print(myData.get_data_in_list())
                

        
    




