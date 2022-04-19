"""
Cette DAO illustre une manière de se connecter à une base de données à partir
d'objets représentant une série.
"""

import sqlite3 as sqlite

from collections import namedtuple

from pyflix import mediamodel as media
from pyflix import conf

SQL_DB_MANAGEMENT = ["CREATE TABLE IF NOT EXISTS shows("
                     "name text NOT NULL, "
                     "PRIMARY KEY (name));"
                     "CREATE TABLE IF NOT EXISTS episodes ("
                     "number integer NOT NULL, "
                     "season integer NOT NULL, "
                     "title text NOT NULL, "
                     "show text NOT NULL, "
                     "duration, "
                     "year, "
                     "PRIMARY KEY(show, number, season), "
                     "FOREIGN KEY (show) REFERENCES shows (name) "
                     "ON DELETE CASCADE);"]

SQL_ADD_SHOW = "INSERT INTO shows values(?)"
SQL_SELECT_SHOWS = "SELECT name FROM shows ORDER BY name"

SQL_ADD_EPISODE = "INSERT INTO episodes values(?, ?, ?, ?, ?, ?)"
SQL_GET_ALL_EPISODES = "SELECT title, season, number " \
                       "FROM episodes " \
                       "WHERE show = ? " \
                       "ORDER BY season, number"
SQL_GET_EPISODES_FOR_SEASON = "SELECT title, season, number " \
                              "FROM episodes " \
                              "WHERE show = ? AND season = ? " \
                              "ORDER BY number"


Episode = namedtuple("Episode", ('title', 'season_number', 'number',
                                 'duration', 'year'),
                     defaults=[None, None])


class MediaDao:
    """
    Cette DAO gère les données au niveau des séries.
    """
    def __init__(self, dbname):
        self._db_name = dbname
        self._connect = sqlite.connect(dbname)

    def __del__(self):
        try:
            self._connect.close()
        except sqlite.Error as e:
            print("Error occured")
            print(e)

    def get_shows(self):
        cur = self._connect.cursor()
        cur.execute(SQL_SELECT_SHOWS)
        return [show[0] for show in cur.fetchall()]


class TvShow:
    """
    Représente une série gérée en base SQLite
    """
    def __init__(self, show_name, dbname):
        """
        La création d'un objet TvShow entraine la création d'un nouvel
        enregistrement en base avec ce nom de série. Si il existait déjà, une
        sqlite.IntegrityError est levée et ignorée par le programme car cette
        exception ne peut être levée que si la série existe déjà.

        :param show_name: Nom de la série (non modifiable)
        :param dbname: Nome de la base SQLite, optionnel.
        """
        self._db_name = dbname
        self._connect = sqlite.connect(dbname)

        try:
            with self._connect:
                try:
                    show_insert_cur = self._connect.cursor()
                    show_insert_cur.execute(SQL_ADD_SHOW, (show_name,))

                except sqlite.IntegrityError:
                    pass  # Le show existe déjà

            self._show_name = show_name

        except sqlite.Error as e:
            print("Error occured")
            print(e)

    def __del__(self):
        try:
            self._connect.close()
        except sqlite.Error as e:
            print("Error occured")
            print(e)

    def __str__(self):
        return f'Media DB Connector ({self._db_name})'

    @property
    def name(self):
        return self._show_name

    @property
    def episodes(self):
        return self.get_episodes()

    def add_episode(self, name: str, season_number: int, ep_number: int,
                    duration: int = None, year: int = None):
        try:
            with self._connect:
                cur = self._connect.cursor()
                cur.execute(SQL_ADD_EPISODE, (ep_number, season_number, name,
                                              self._show_name, duration, year))
        except sqlite.IntegrityError:
            raise ValueError(f"Duplicate episode s{season_number}e{ep_number}")

    def get_episodes(self, season_number=None):
        """
        Retourne une liste d'épisodes
        :return: liste d'objets de type mediamodel.Episode
        """
        cur = self._connect.cursor()
        if season_number:
            cur.execute(SQL_GET_EPISODES_FOR_SEASON, (self._show_name,
                                                      season_number))
        else:
            cur.execute(SQL_GET_ALL_EPISODES, (self._show_name,))

        return [media.Episode(title, episode_number, season_number)
                for title, season_number, episode_number in cur.fetchall()]


def configure_db(db_path):
    """
    Fonction destinée à paramétrer la base de données en gérant sa
    version.

    Lorsque ce module est importé au lancement du programme, cette
    fonction est appelée. Elle crée une connexion à la base et vérifie
    sa version. SQLite permet de gérer des versions avec les pragma. Si
    la version est inférieur au nombre de scripts dans la liste
    SQL_DB_MANAGEMENT, les scripts à partir de l'indice de version sont
    exécutés. Ceci facilite l'évolution de la structure de la base :
    la faire évoluer consiste à ajouter le script SQL d'évolution dans la
    liste.
    :param db_path: Chemin vers la base de données.
    """
    connect = sqlite.connect(db_path)

    cur = connect.cursor()
    cur.execute("pragma user_version")
    user_version_value = cur.fetchone()[0]
    if user_version_value < len(SQL_DB_MANAGEMENT):
        for statement in SQL_DB_MANAGEMENT[user_version_value:]:
            cur.executescript(statement)

        cur.execute(f"pragma user_version={len(SQL_DB_MANAGEMENT)}")

    connect.close()


configure_db(conf.SQLITE_PATH)
