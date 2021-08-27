#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ce module contient les outils pour charger les données média à partir de
fichiers.
"""

import re
import os

SERIES_RE = re.compile("-s([0-9]{2})e([0-9]{2})-")

def get_show_values_from_filename(filename):
    """
    Retourne les informations d'une série à partir d'un nom de fichier (sans
    l'extension).

    :param filename: nom du fichier sans l'extension.
    :return: Un tuple contenant le nom de la série, le numéro de la saison,
    numéro d'épisode et titre ou None si le motif utilisé n'est pas trouvé.
    """
    series_match = SERIES_RE.search(filename)
    if series_match:
        return filename[:series_match.start()].replace('_', ' '), \
               series_match.group(1), \
               series_match.group(2), \
               filename[series_match.end():].replace('_', ' ')


def get_series_value_from_filenames(dir_path):
    """
    Retourne les données sur un épisode. Les valeurs sont :
    * Nom de la série
    * Numéro de la saison
    * Numéro de l'épisode
    * Titre de l'épisode
    * None (durée)
    * None (année)

    :param filename: nom du fichier duquel extraire les données
    :return: une liste de chaines de caractères, voir description.
    :return type: tuple
    """
    for item in os.scandir(dir_path):
        series_file_name, series_ext = os.path.splitext(item.name)

        show_data = get_series_value_from_filenames(series_file_name)
        if show_data:
            yield *show_data, None, None
        else:
            pass  #TODO: Un log devrait être ajouté

def get_series_values_from_csv(filepath):
    """
    Retourne les données sur un épisode. Les valeurs sont :
    * Nom de la série
    * Numéro de la saison
    * Numéro de l'épisode
    * Titre de l'épisode
    * Durée
    * Année


    :param record: nom du fichier duquel extraire les données
    :return: une liste de chaines de caractères, voir description.
    :return type: tuple
    """

    with open(filepath, 'r') as media_file:
        media_file.readline()

        for media in media_file:
            yield tuple(media[:-1].split(";"))


def load_episode_from_file(filepath):
    """
    Cette fonction va charger les informations des médias.

    Si `filepath` est un répertoire, les informations seront extraites du mon
    des fichiers sinon à partir du contenu du fichier.

    :param filepath: Chemin vers le fichier contenant les noms de fichiers épisodes
    :return: Une liste de tuples (titre série, numéro série, numéro épisode, titre épisode)
    :raise OSError: if file does not exist.
    """

    if os.path.isdir(filepath):
        get_series_values = get_series_value_from_filenames
    else:
        get_series_values = get_series_values_from_csv

    for media in get_series_values(filepath):
        yield media


if __name__ == '__main__':

    import argparse

    SERIES_FULL_NAME = "Silicon_Valley-s01e03-Articles_Of_Incorporation.avi"

    PARSER = argparse.ArgumentParser(description='')
    PARSER.add_argument("-f", "--file", help="Path to the file to parse",
                        type=str, action="store")

    ARGS = PARSER.parse_args()

    if ARGS.file:
        for media in load_episode_from_file(ARGS.file):
            print(media)
    else:
        print(get_series_value_from_file(SERIES_FULL_NAME))
