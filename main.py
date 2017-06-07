"""
main.py

Pourquoi ? :
Ce module est le module principal. C'est lui qui va exploiter les ressources que
nous sommes allés chercher et que nous avons construites avec les autres modules
pour dessiner la carte.

"""
import sys
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
sys.path.append(".")
from numpy_saver_and_loader import load
from histogramme import display_histo

# On importe les dictionnaires préalablements sauvegardés avec
# numpy_saver_and_loader

DICT_COUNTRY_LOCATION = load("DICT_COUNTRY_LOCATION").item()
DICT_COUNTRY_BILL_NBR = load("DICT_COUNTRY_BILL_NBR").item()

# on forme à partir des dictionnaires précédents les listes de variables utiles
# pour dessiner la carte
BILL_NUMBER = []
for country in DICT_COUNTRY_BILL_NBR:
    BILL_NUMBER.append(DICT_COUNTRY_BILL_NBR.get(country))

LATS = []
LONGS = []

for country in DICT_COUNTRY_LOCATION:
    LATS.append(DICT_COUNTRY_LOCATION.get(country).get("lat"))
    LONGS.append(DICT_COUNTRY_LOCATION.get(country).get("lng"))

# On récupère la valeur minimale de la liste des valeurs pour créer plus tard
# un tableau de la tailles des points que nous afficherons

NBR_MIN_BILL_COUNTRY = min(DICT_COUNTRY_BILL_NBR.values())

# Création de la figure contenant la carte
FIG = plt.figure()
FIG.canvas.set_window_title("Carte")

# Mise en place du fond de carte
THE_MAP = Basemap()
THE_MAP.bluemarble()
THE_MAP.drawcountries()
THE_MAP.drawcoastlines()
# Conversion des coordonnées géographiques en coordonnées graphiques
X, Y = THE_MAP(LONGS, LATS)

# On récupère un dégradé de couleur que l'on utilisera pour donner une couleur
# aux points en fonction de leurs valeurs
CMAP = plt.cm.get_cmap('autumn')

# Construction d'un tableau contenant les tailles des points affichés (dont on
# aura réglé les valeurs afin d'avoir une carte la plus lisible possible)
SIZE = (np.array(BILL_NUMBER)-NBR_MIN_BILL_COUNTRY+1)*2

# Affichage des points avec les paramètres préalablements mis en place
SCA = THE_MAP.scatter(X, Y, s=SIZE, marker='o', c=BILL_NUMBER, cmap=CMAP)

# Affichage du titre et de l'échelle de valeurs avec son dégradé de
# couleurs associé
plt.title(('La répartition inégale des milliardaires dans le monde,'
           'par pays, en 2015'))
plt.colorbar(SCA)

# Affichage de la carte et de l'histogramme
display_histo(plt)
plt.show()
