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

    
    def get_data_in_list(self, first_line:bool=False) -> List[List[str]]:
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
    
    def get_data_in_list_of_numbers(self) -> List[List[int]]:
        """
        Remove all units from the data and returning only the list of numbers (as get_data_in_list() but without units)

        Returns:
            List[List[int]]: The data once formated
        """
        
        numbers : List[int] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        number : str = ""
        data : List[List[str]] = self.get_data_in_list()
        newList : List[List[int]] = []
        
        for line in range(len(data)):
            newList.append([])
            for element in range(len(data[line])):
                number = ""
                for char in range(len(data[line][element])):
                    if data[line][element][char] in numbers:
                        number += data[line][element][char]
                newList[-1].append(int(number))
        
        return newList
                        

    def average_time_diff(self, column:int=0) -> float:
        """
        Calcule le temps moyen entre 2 lignes du fichier csv, la colonne contenat le temps est précisé avecle paramètre column

        Args:
            column int (default to 0): La position de la colonne indiquant le temps
        
        Returns:
            float: Le temps moyen
        """
        
        data = self.get_data_in_list()
        average_time : int = 0
        
        for i in range(1, len(data)):
            average_time += int(data[i][column]) - int(data[i-1][column])
        
        return average_time / (len(data) - 1)




            


if __name__ == '__main__':
    myData = data_handler("../data.csv")
    
    print(myData.get_raw_data_in_string())
    print(myData.get_data_in_list())
    print(myData.average_time_diff())
    print(myData.get_data_in_list_of_numbers())
                

        
    




