"""
Module de configuration du programme.

Le principe du module de configuration repose sur le fait qu'un module n'est
chargé qu'une seule fois. Le module principal va donc charger ce module de
configuration et modifier les variables en fonction des paramètres de
lancement. Par la suite, chaque module qui charge ce module de configuration
accèdera à la bonne valeur de paramètre.
"""

from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent

# PATHs
SQLITE_PATH = ROOT_PATH / "default.db"
