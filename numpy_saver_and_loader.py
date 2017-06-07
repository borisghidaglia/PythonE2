"""
numpy_saver_and_loader.py

Pourquoi ? :
Ce module sert à sauvegarder des objets que nous avons pu créer avec nos
modules de scraping et/ou de parsing, puis à les charger dans les modules qui en
ont l'utilité. Nous avons créé ce module plutôt que d'utiliser directement
les fonctions de numpy afin de pouvoir expliciter et justifier
ici leur utilisation.

Contenu:
Contient deux fonctions : save(), load()

"""
import numpy as np

def save(name_file, element):
    """
    Sauvegarde l'objet passé en paramètre avec le nom de fichier passé en
    paramètre.

    Args:
        name_file : le nom de fichier voulu pour la sauvegarde
        element : l'objet à sauvegarder

    """
    np.save(name_file+".npy", element)

def load(name_file):
    """
    Charge l'objet voulu à l'aide du nom du fichier qui le contient, passé en
    paramètre.

    Args:
        name_file : le nom de fichier dont on veut charger l'objet

    Returns:
        object
    """
    return np.load(name_file+".npy")
