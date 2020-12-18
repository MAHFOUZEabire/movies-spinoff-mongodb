# utils.py
import csv
from datetime import datetime 

def lire_csv_dict(nom_fichier):
    data = []
    with open(nom_fichier, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def lire_csv_liste(nom_fichier):
    data = []
    with open(nom_fichier, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        entete = next(reader)
        for row in reader:
            data.append(row)
    return data, entete

def renvoyer_annee_titre_film(title):
    """ 
    Fonction renvoyant l'année du film et son titre seul (sans année)
    
    Exemple: 
        utils.renvoyer_annee_titre_film('Toy Story (1995)')
    renvoie:
        (1995, 'Toy Story')
    """
    new_title = title.strip()
    year = int(new_title[-5:-1])
    new_title = new_title[:-6].strip()

    return year, new_title

def renvoyer_datetime_iso(timestamp):
    """ 
    Fonction renvoyant la date & l'heure au format iso
    
    Exemple: 
        utils.renvoyer_datetime_iso(964982703)
    renvoie:
        '2000-07-30T20:45:03'
    """
    return None