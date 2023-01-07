#!/usr/bin/python

"""!

@brief Traitement des données d'un fichier csv

@package traitement

@file graphs.py
Traitement d'un fichier csv

@version 1.0

@section author_libraries_devises Author(s)
- Crée par Guyon Brewal le 03/01/2023.
- Copyright (c) 2022 IUT de Lannion. All rights reserved.
"""




import csv
import os
from typing import List, Tuple

# changement du repertoire d'execution du fichier
directory = os.path.dirname(__file__)
print(f"Execution du fichier dans {directory}")

os.chdir(directory)

class data_handler:
    """! Classe qui va servir a interagir avec le fichier csv
    """

    def __init__(self, filename:str, separateur=',') -> None:
        """! Creation de la classe qui va servir aux interactions avec le fichier csv
        
        @param filename  nom du fichier csv a charger
        @param separateur  separateur des colonnes du fichier csv
        """
        self.separateur : str = separateur
        
        self.filename : str = filename
        
        self.lines : List[str] = []
        
        self.raw : str = ""
        
        with open(filename, newline='') as csvfile :
            datareader : csv._reader = csv.reader(csvfile, delimiter=self.separateur, quotechar='|')
            
            for line in datareader:
                # ajouter les lignes a la liste
                self.lines.append(line)
                
                # ajouter les lignes sous la forme de string dans le string
                self.raw += ",".join(line) + "\n"
        
    def get_raw_data_in_string(self) -> str:
        """! Renvoie les données brutes du fichier csv en format string
        
        @return  les données du fichier en dur
        """
        return self.raw

    
    def get_data_in_list(self, first_line:bool=False) -> List[List[str]]:
        """! Renvoie une liste a 2 dimensions qui contient les differentes donnees en string
        
        Exemple pour le fihier csv
        a, b, c
        d, e, f
        g, h, i
        
        >> [[a, b, c], [d, e, f], [g, h, i]]
        
        @param first_line  si first_line est a False alors la premier ligne n'est pas prise en compte

        @return  la liste de liste représentant les donées
        """
        return self.lines[1:] if not first_line else self.line
    
    def get_data_in_list_of_numbers(self) -> List[List[int]]:
        """! Enlève les unitées si il y en a (comme get_data_in_list() mais sans unitées)
        
        @return  la liste de liste contenant les données
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
                        

    def average_diff(self, column:int=0) -> float:
        """! Calcule la différence moyenne dans une colonne (par défaut la première colonne)

        @param column  La colonne sur la quelle il faut réaliser l'oppération
        
        @return  La différence moyenne
        """
        
        data = self.get_data_in_list()
        average_time : int = 0
        
        for i in range(1, len(data)):
            average_time += int(data[i][column]) - int(data[i-1][column])
        
        return average_time / (len(data) - 1)
    
    def average(self, column:int) -> float:
        """! Calcule la moyenne d'une colonne

        @param column  indice de la colonne

        @return  moyenne de la colonne
        """
        
        # donnees sans unitées
        data = self.get_data_in_list_of_numbers()
        average : int = 0
        
        for line in range(len(data)):
            average += data[line][column]
        
        return average / len(data)
    
    def get_name(self, column:int) -> str:
        """! Renvoie le nom d'une colonne

        @param column  indice de la colonne

        @return  nom de la colonne
        """
        
        return self.lines[0][column]
    
    def get_column(self, column:int) -> List[int]:
        """! Renvoie la colonne en parametre sous forme de liste

        @param column  indice de la colonnne

        @return  Liste contenant les valeurs de la colonne
        """
        
        data = self.get_data_in_list_of_numbers()
        
        result : List[int] = []
        
        for line in range(len(data)):
            result.append(data[line][column])
        
        return result
    
    def min_max(self, column:int) -> Tuple[float, float]:
        """! Renvoie le couple max, min d'une colonne donnée

        @param column  La colonne en question.

        @return  Le couple max, min
        """
        data = self.get_data_in_list_of_numbers()
        max, min = data[column][0], data[column][0]
        
        for i in range(1, len(data)):
            if data[i][column] > max:
                max = data[i][column]
                
            if data[i][column] < min:
                min = data[i][column]
        
        return min, max
    

    def get_data_in_dict(self, column) -> dict:
        """! Récuperer les données sous la forme d'un dictionnaire avec la colonne en paramètre comme clés
        
        @param column  indice de la colonne clés
        
        @return  dictionnaire avec les données
        """
        
        
        data : List[List[int]] = self.get_data_in_list_of_numbers()
        
        dictionnaire : dict = {}
        
        for i in range(len(data)):
            dictionnaire[data[i][column]] = data[i]
            
        return dictionnaire
    
    
    def get_max_by_refernce(self, column_ref, column_aim) -> int:
        """!Renvoi la valeur de la colonne column_ref pour la valeur max de column_aim
        
        @param column_ref  colonne qui contient la valeur qui va etre renvoyée
        @param column_aim  colonne qui contient les valeurs de référence (c'est ici que le max va etre recherché)

        @return  la valeur trouvé
        """
        
        data : dict = self.get_data_in_dict(column_ref)
        
        max = (list(data.keys())[0], data[list(data.keys())[0]][column_aim])
        
        for key,values in data.items():
            
            if max[1] < values[column_aim]:
                max = (key, values[column_aim])
                
        return max[0]
            
            
        



            


if __name__ == '__main__':
    myData = data_handler("../data.csv")
    
    print(myData.get_raw_data_in_string())
    print(myData.get_data_in_list())
    print(myData.average_diff())
    print(myData.get_data_in_list_of_numbers())
    print(myData.average(2))
    print(myData.get_name(2))
    print(myData.get_column(2))
    print(myData.min_max(0))
    print(myData.get_data_in_dict(0))
    print(myData.get_max_by_refernce(0, 3))

        
    




