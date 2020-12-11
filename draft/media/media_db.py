#!/usr/bin/env python

"""
Module de gestion de connexion à une base de données.

Note sur la présence de la fonction print :
Un objet ne doit pas avoir une instruction print car on ignore son contexte
d'exécution. Néanmoins, un objet comme la DAO doit conserver des "traces" des
évènements. Ceci passe communément par des loggers. Ce code étant destiné à des
formations ne traitant en général pas les loggers, un print est utilisé à la
place.
"""

import sqlite3 as sqlite

SQL_CREATE_EPISODES_TABLE = "CREATE TABLE IF NOT EXISTS episodes ("\
                            "e_number INT NOT NULL, "\
                            "season INT NOT NULL, "\
                            "title TEXT NOT NULL, "\
                            "PRIMARY KEY (e_number , season))"

SQL_ADD_EPISODE = "INSERT INTO episodes values(?, ?, ?)"
SQL_GET_EPISODE = "SELECT title, season, e_number FROM episodes where season = ? and e_number = ?"
SQL_GET_ALL_EPISODES = "SELECT title, season, e_number FROM episodes ORDER BY season, e_number"
SQL_GET_EPISODES_FOR_SEASON = "SELECT title, season, e_number FROM episodes where season = ? ORDER BY e_number"


class TvShowDao:
    def __init__(self, dbname="test"):
        import re
        self._db_name = re.sub("[ .()]", "_", dbname) + '.db'  # Voir regex
        self._connect = sqlite.connect(self._db_name)

        try:
            cur = self._connect.cursor()
            cur.execute(SQL_CREATE_EPISODES_TABLE)

        except sqlite.Error as e:
            print("Error occured")  # Voir docstring à propos du print
            print(e)  # Voir docstring à propos du print

    def __del__(self):
        try:
            self._connect.close()

        except sqlite.Error as e:
            print("Could not close database")  # Voir docstring à propos du print
            print(e)  # Voir docstring à propos du print

    def __str__(self):
        return 'Media DB Connector ({})'.format(self._db_name)

    def add_episode(self, title: str, ep_number: int, season_number: int):
        """
        Ajoute un épisode à la collection.

        :param title: titre de l'épisode
        :param ep_number: numério de l'épisode
        :param season_number: numéro de saison de l'épisode
        :raises ValueError: si l'épisode existe déjà
        """
        try:
            with self._connect:
                cur = self._connect.cursor()
                cur.execute(SQL_ADD_EPISODE, (ep_number, season_number, title))
        except sqlite.IntegrityError:
            raise ValueError(f"Episode {title} s{season_number}e{ep_number} axists")