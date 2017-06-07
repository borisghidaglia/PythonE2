"""
histogramme.py

Pourquoi ? :
Ce module va construire un histogramme liant les milliardaires en fonction de
leurs fortunes. Ainsi nous pourrons observer les inégalités entre eux.

"""
import sys
import numpy as np
import matplotlib.pyplot as pyplot
sys.path.append(".")
from numpy_saver_and_loader import load

def display_histo(plt):
    """
    Gère les appels des fonctions qui vont créer l'histogramme

    Args:
        plt : afin de créer une seconde figure sur le même plt que la carte
        qui elle, sera la figure 1

    """
    # On importe les dictionnaires préalablements sauvegardés avec
    # numpy_saver_and_loader
    fortunes = load('fortunes')
    # On appelle chaque fonction
    init(plt, fortunes)
    values_histo = calc(fortunes)
    plot(values_histo, plt, fortunes)

def init(plt, fortunes):
    """
    Crée la figure, lui donne un titre, puis défini les valeurs à placer sur
    les axes de l'histogramme à partir des valeurs min et max de la liste
    contenant les fortunes

    Args:
        plt : afin de pouvoir agir sur l'objet
        fortunes : contient la liste des fortunes de milliardaires

    """
    fig = plt.figure()
    fig.canvas.set_window_title("Histogramme")
    # Etendue de l'histogramme et mise en place de celui-ci
    mini = int(min(fortunes))
    maxi = int(max(fortunes) + 2)
    scope = list(range(mini, maxi, 1))
    plt.hist(fortunes, bins=scope)
    plt.xlabel("Fortune en milliards de dollars")
    plt.ylabel("Nombre de milliardaire possédant cette fourchette de fortune")
    plt.title("""Répartition inégales des richesses au sein même de la
              communauté des milliardaires en 2015""")


def calc(fortunes):
    """
    Calcule et retourne les données qui seront nécessaires pour construire
    l'histogramme en se basant sur les valeurs de fortunes

    Args:
        fortunes : contient la liste des fortunes de milliardaires

    Returns:
        values_histo : [moyenne, mediane, quartile, ecart_type, variance]

    """
    # Calculs et affichage des valeurs remarquables
    # Tri par ordre croissant afin de calculer plus facilement
    fortunes.sort()
    moyenne = round(sum(fortunes)/len(fortunes), 2)
    mediane = round(np.median(fortunes), 2)
    quartile = round(np.median(fortunes[:int(len(fortunes) / 2)]), 2)
    ecart_type = round(np.std(fortunes), 2)
    variance = round(np.var(fortunes), 2)
    values_histo = [moyenne, mediane, quartile, ecart_type, variance]
    return values_histo

def plot(values_histo, plt, fortunes):
    """
    Crée la légende de l'histogramme en se basant sur les valeurs calculées
    dans calc et sur la valeur maximum de fortunes.

    Args:
        values_histo : contient la liste des valeurs calulées dans calc
        plt : afin de pouvoir agir sur l'objet
        fortunes : contient la liste des fortunes de milliardaires

    """
    moyenne, mediane, quartile, ecart_type, variance = values_histo
    plt_moyenne = plt.axvline(x=moyenne, linewidth=3, color='r')
    plt_mediane = plt.axvline(x=mediane, linewidth=3, color='pink')
    plt_quartile = plt.axvline(x=quartile, linewidth=3, color='yellow')
    plt_maxi = plt.axvline(x=max(fortunes), linewidth=5, color="green")
    # Affichage nul sur la figure mais nécessaire pour construire la légende
    plt_ecart_type = plt.axvline(x=0, linewidth=0, color='black')
    plt_variance = plt.axvline(x=0, linewidth=0, color='black')
    plt.legend([plt_moyenne,
                plt_mediane,
                plt_quartile,
                plt_maxi,
                plt_ecart_type,
                plt_variance], [
                    'moyenne = {}'.format(moyenne),
                    'mediane = {}'.format(mediane),
                    '1er quartile = {}'.format(quartile),
                    'maxi = {}'.format(round(max(fortunes), 2)),
                    'ecart type = {}'.format(ecart_type),
                    'variance = {}'.format(variance)], loc='right')


if __name__ == '__main__':
    display_histo(pyplot)
    pyplot.show()
    #pyplot.savefig("histogramme.png")
