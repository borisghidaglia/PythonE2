"""
locations.py

Pourquoi ? :
Ce module va récupérer depuis le dictionnaire DICT_COUNTRY_BILL_NBR précédemment
sauvegardé, tous les pays dans lesquels on trouve des millairdaires. Ensuite, il
va effectuer une requête pour récupérer un JSON qu'il va parser pour trouver les
coordonnées de ces pays. Enfin, il va stocker dans un dictionnaire le nom de ce
pays avec ses coordonnées propres, puis sauvegardé le dictionnaire ainsi créé
pour pouvoir le réutiliser dans notre module principal.

Contenu:
Ne contient qu'une seule fonction : scraping_country_locations()

"""
import urllib.request
import json
import sys
sys.path.append(".")
from numpy_saver_and_loader import save, load

def scraping_country_locations():
    """
    Retourne un dictionnaire contenant des noms de pays associés à leurs
    coordonnées propres (elles même situées dans un dictionnaire).
    Appeler directement le module pour construire/reconstruire le dictionnaire
    de valeurs.

    Args: aucun

    Returns:
        dict = {'France': {'lat': 46.227638, 'lng': 2.213749},...}

    """
    dic_country_location = dict() #country location

    for country in load("DICT_COUNTRY_BILL_NBR").item():
        country_for_request = country.replace(" ", "%20")
        api_key = "AIzaSyDI7W4OufmP3hgsBgXtsD_qgm7uWwFAMKs"
        request = ("https://maps.googleapis.com/maps/api/geocode/json?"
                   "address={0}&key={1}").format(country_for_request, api_key)
        with urllib.request.urlopen(request) as response:
            html = response.read().decode('utf-8')
            dict_temporary = json.loads(html)
            country_location =\
                dict_temporary["results"][0]["geometry"]["location"]
            dic_country_location[country] = country_location
    return dic_country_location

if __name__ == '__main__':
    DICT_GENERATED = scraping_country_locations()
    # save("DICT_COUNTRY_LOCATION", DICT_GENERATED)
    # test ESIEE
    save("DICT_COUNTRY_LOCATION", DICT_GENERATED)
