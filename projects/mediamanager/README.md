# Vers PyFlix

Ce projet illustre un résultat final qui peut être vu en formation. Le sujet
est d'aller vers la mise en place d'une plate-forme media. La finalité pourra
aussi bien être un mediacenter personnel qu'un service commercial.

## Usage
Le point d'entrée de cette application est le module `mediamanager.main`.
Celui-ci doit être lancé d'un shell avec une commande. Les commandes sont :
 * **load** : lance le programme de chargement des données
 * **web** : lance la webapp locale
 * **app** : lance l'application tkinter

Note : les fichiers *launcher* en `.bat` et `sh` lancent la webapp avec tous
les paramètres par défaut.

## Précisions techniques
### Configuration de l'application
Les paramètres de l'application sont dans le module `mediamanager.conf`. Ce
module conient la configuration par défaut. Il doit être importé dans le
*programme principal* et modifié en fonction des paramètres de lancement de
l'application. Ce module doit ensuite être importé dans les modules où ces
paramètres seront nécessaires et son conenu sera donc disponible. 

### Configuration de la base de données
Cette application utilise une base de données SQLite.

Le module `mediamanager.media_db` contient tout le nécessaire à l'utilisation
d'une base de données. Les scripts SQL sont déclarés dans ce module. La logique
de création, évolution et maintenance est expliquée dans le module.

### Options de la ligne de commande
Cette application utilise les arguments de la ligne de commande. L'utilisation
de ces argument est géré dans le module `mediamanager.main` avec `argparse`.