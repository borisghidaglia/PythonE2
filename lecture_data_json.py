"""
lecture_data_json.py

Pourquoi ? :
Ce module utilisera le module numpy_saver_and_loader.py qui sauvegardera
le dictionnaire DICT_GENERATED généré dans le __main__.
Ainsi, nous n'aurons plus qu'à charger le dictionnaire dans le programme
principal main.py. Cela nous évite d'avoir à appeler ce module qui parserait
à chaque fois le même fichier, très long et très lourd.
Appeler directement le module pour construire/reconstruire le dictionnaire
de valeurs.

Contenu:
Ne contient qu'une seule fonction : json_parsing()

"""
import json
import sys
sys.path.append(".")
from numpy_saver_and_loader import save



def json_parsing(name_file):
    """
    Retourne un dictionnaire contenant des noms de pays associés au nombre de
    milliardaires qu'il contient et crée une liste contenant les valeurs des
    fortunes des milliardaires afin de les réutiliser pour l'histogramme.


    Args:
        name_file : le nom du fichier json à parser

    Returns:
        dict = {'France' : 78,...}
    """
    # contient un nombre de milliardaires pour chaque pays trouvé dans le JSON
    dico_country_billionaire_number = dict()
    # contient le nom d'un milliardaire associé à sa plus grande fortune dans
    # les données (en effet il arrive que dans les données un même milliardaire
    # possède deux champs à son nom contenant deux valeurs différentes de
    # fortunes et ce même sur la même année)
    name_fortune = dict()
    # contient la liste des valeurs des fortunes des millairdaires
    fortunes = list()
    # On ouvre le fichier puis on charge son JSON pour obtenir un dictionnaire
    # que l'on pourra exploiter
    with open(name_file) as data_file:
        data = json.load(data_file)
        # je parcours tous les "records" du fichier json qui contiennent chacun
        # un milliardaire
        for billionaire in range(len(data["records"])):
            # Récupération des variables contenant le pays,le nom et la fortune
            # du milliardaire
            country = data["records"][billionaire]["fields"].get("citizenship")
            name = data["records"][billionaire]["fields"].get("name")
            fortune = data["records"][billionaire]["fields"].get("realnetworth")
            year = int(data["records"][billionaire]["fields"].get("year"))
            # On vérifie que le milliardaire est bien miliardaire (certains ont
            # moins d'un milliard dans les données) en 2015
            if fortune != None and fortune >= 1 and year == 2015 and country != None:
                # Si le nom n'est pas dans la liste on l'ajoute, lié à sa
                # fortune
                # Sinon on actualise la valeur de la fortune si celle-ci est
                # supérieure
                if name not in name_fortune:
                    name_fortune[name] = fortune
                    # Si nous sommes ici c'est qu'un nouveau milliardaire a
                    # été ajouté, on regarde si son pays aussi est nouveau
                    # si il n'existe pas de valeur associée au pays, c'est
                    # qu'il n'a pas encore été ajouté alors on l'ajoute
                    if dico_country_billionaire_number.get(country) is None:
                        dico_country_billionaire_number[country] = 0
                    # On incrémente sa valeur de 1
                    dico_country_billionaire_number[country] += 1
                elif fortune > name_fortune.get(name):
                    name_fortune[name] = fortune
        # On crée la liste des fortunes avec les fortunes contenues dans le
        # dictionnaire name_fortune
        for name in name_fortune:
            fortunes.append(name_fortune.get(name))
        return dico_country_billionaire_number, fortunes

if __name__ == '__main__':
    # On génère le dictionnaire et la liste retournés par json_parsing et
    # on le sauvegarde
    DICT_GENERATED, FORTUNES = json_parsing('dataBillionaire.json')
    save("DICT_COUNTRY_BILL_NBR", DICT_GENERATED)
    save("FORTUNES", FORTUNES)
