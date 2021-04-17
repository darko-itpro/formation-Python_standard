#!/usr/bin/env python

"""
Ce module illustre un launcher pour l'application media. Celui-ci gère les
paramètres passés à la ligne de commande et permet l'exécution des différentes
interfaces en fonction d'un paramètre command.

Work in progress

"""

from mediamanager import conf

def launch_app(_):
    # Manière simple de lancer l'interface tkinter
    import mediamanager.media_tk


def launch_webapp(args):
    import mediamanager.mediaweb as webapp
    webapp.app.run()


def load_data(args):
    import mediamanager.media_file_loader as loader
    import mediamanager.media_db as db

    db_name = args.db_path

    for show_name, season, number, title, *_ in loader.load_episode_from_file(args.file):
        show = db.TvShow(show_name, db_name, conf.SQLITE_PATH)
        show.add_episode(title, season, number)


if __name__ == '__main__':

    actions = {"web": launch_webapp,
               "app": launch_app,
               "load": load_data}

    import argparse

    PARSER = argparse.ArgumentParser(
        description="Gestion de médiathèque. Par défaut, la gestion des données"
                    " est assurée par une base de données."
    )

    PARSER.add_argument("command", choices=list(actions),
                        help="Lance le programme en cli, web, app (Tkinter) ou "
                             "charge simplement des données en base.")

    PARSER.add_argument('-s', '--statefull', action='store_true',
                        help="Force l'utilisation du modèle objet. "
                             "La base de données est ignoré.")
    PARSER.add_argument('-p', '--db_path', default="default.db",
                        help='Chemin vers le fichier de la base')
    PARSER.add_argument('-f', '--file', help="Chemin vers le fichier contenant "
                                             "des données.")

    ARGS = PARSER.parse_args()

    conf.SQLITE_PATH = ARGS.db_path  #  Pourrait être validé

    actions[ARGS.command](ARGS)