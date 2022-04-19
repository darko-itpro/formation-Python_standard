#!/usr/bin/env python

"""
Ce module illustre un launcher pour l'application media. Celui-ci gère les
paramètres passés à la ligne de commande et permet l'exécution des différentes
interfaces en fonction d'un paramètre command.

Work in progress

"""

from pyflix import conf
import argparse


def launch_app(_):
    # Manière simple de lancer l'interface tkinter
    pass


def launch_webapp(args):
    import pyflix.mediaweb as webapp
    webapp.app.run()


def display_cli(_):
    import pyflix.ui.cli as cli
    import pyflix.media_db as db

    shows = db.MediaDao(conf.SQLITE_PATH)
    cli.display_shows({name: db.TvShow(name, conf.SQLITE_PATH)
                       for name in shows.get_shows()})


def load_data(args):
    import pyflix.media_file_loader as loader
    import pyflix.media_db as db

    db_name = args.db_path

    try:
        for show_name, season, number, title, duration, year \
                in loader.load_episode_from_file(args.file):
            show = db.TvShow(show_name, conf.SQLITE_PATH)
            show.add_episode(title, season, number, duration, year)
    except TypeError as e:
        import sys
        if args.file is None:
            print("Erreur :")
            print(">>> L'option --file est indispensable avec la commande load")
        else:
            print('>>> Erreur de type TypeError inconnue')
            print(e)
        sys.exit(1)

    except FileNotFoundError:
        print("Erreur :")
        print(f">>> Le fichier '{args.file}' n'a pas été trouvé.")
        import sys
        sys.exit(1)


def read_user_cli_args():
    PARSER = argparse.ArgumentParser(
        description="Gestion de médiathèque. Par défaut, la gestion des données"
                    " est assurée par une base de données."
    )

    PARSER.add_argument("command", choices=list(actions),
                        help="Lance le programme en web, app (Tkinter) ou "
                             "charge simplement des données en base.")

    PARSER.add_argument('-p', '--db_path', default="default.db",
                        help='Chemin vers le fichier de la base')
    PARSER.add_argument('-f', '--file', help="Chemin vers le fichier contenant "
                                             "des données.")

    return PARSER.parse_args()


actions = {"web": launch_webapp,
           "app": launch_app,
           "load": load_data,
           "display": display_cli,
           }


ARGS = read_user_cli_args()

conf.SQLITE_PATH = ARGS.db_path  #  Pourrait être validé

actions[ARGS.command](ARGS)