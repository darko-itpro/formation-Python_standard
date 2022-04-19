# A Python Training - PyFlix

This is the practical cases for Python training I provide. Intended for french
trainee, the rest of the explanations are in french.

Ce référentiel complète la formation que je propose et est donc destiné à
mes stagiaires. 

[![License](https://img.shields.io/github/license/darko-itpro/training-python.svg?style=plastic)](https://github.com/darko-itpro/training-python/blob/master/LICENSE)

![GitHub last commit](https://img.shields.io/github/last-commit/darko-itpro/formation-Python_standard)

Ces sources représentent un projet de référence pour une formation Python. Il couvre aussi bien les
fondamentaux que des notions avancées.

Ces sources sont en cours de réorganisation, le contenu de ce README n'est pas à jour. 

## Organisation des sources
Ces sources ne sont pas **un** projet mais plusieurs. Les projets sont dans le
répertoire `projects`.  L'organisation (à terme) est la suivante :
 * `assets` : contient les ressources pour les exercices.
 * `pyflix` : est le projet décrit ci-dessous
 * `tests` : est le package contenant des tests.

## Mise en place de l'environnement

### Prérequis
[Python](https://www.python.org) doit être installé. La formation est prévue pour être compatible
Python 3.6+ mais des exemples illustrent des fonctionnalités plus récentes.

### Récupérez le projet
Récupérez ce projet en local. En fonction de vos outils et de vos connaissances de Git,
clonez le répertoire ou récupérez les sources sous forme d'archive zip. Vous pouvez placer
le projet où vous le souhaitez dans votre arborescence.

### Installez les dépendances
[pip](https://pypi.python.org/pypi/pip) est le gestionnaire de dépendances qui
va nous permettre d'installer tout ce qui est nécessaire à ce projet. Vous
pouvez évidemment travailler dans un [virtualenv](https://virtualenv.pypa.io/en/stable/)
dédié à la formation. Si vous utilisez un IDE tel que PyCharm, vous pouvez
l'utiliser pour créer ce virtualenv. Placez vous alors à la racine du projet et
saisissez

```
python -m pip install -r requirements.txt
```

Votre environnement contient alors toutes les dépendances nécessaires. Il ne
reste plus qu'à générer la documentation (optionnel).

### Générez la documentation
Le répertoire /docs/ contient un exemple de documentation de projet. Pour la générer,
Placez-vous dans ce répertoire et exécutez
 
```
make html
```

La documentation est alors dispoible dans le sous répertoire *_build/html*.

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

## Exercices pratiques

Ces sources contiennet des propositions de *corrections* des exercices pratiques
proposés en formation. Leur objectif principal est d'illustrer ce qui a été
présenté en formation. Les répertoires d'intérêt sont :
* `/training/projects` propose plusieurs projets regroupés en packages.
    * `/bank` sur le thème de la gestion de comptes bancaires contient
      principalement du code tel que présent dans le support. 
    * `/mediamanager` contient un projet complet de gestion de médiathèque.
    * `/museums` contient un projet de maniulation de données sur les musées
    * `/sncf` contient un projet de manipulation de données issues de la SNCF
    * `/stacks` propose un exemple d'implémentation de piles
    * `/trainig` sur le thème de la gestion de fomrations reprends le code du
      support.
* `/training/cases` est un package contennat des modules illustrant des outils
    présentés durant la formation
    
### MediaManager
Le projet MediaManager est le plus aboutit, il s'agti du fil directeur le plus
régulièrement utilisé durant mes formations. Vous pouvez tester les exemples en
lançant les différents modules. Les commandes les plus pratiques seront :

```
python -m training.projects.mediamanager.mediamanager load -f assets/showslist.csv
``` 

qui permet de créer la base de données et de l'alimenter avec les informations du
fichier csv.

```
python -m training.projects.mediamanager.mediamanager cli
```

lance l'interface en ligne de commande.

```
python -m training.projects.mediamanager.mediamanager app
```

lance l'interface tkinter. Cette interface n'est pas connectée à la base de données,
elle ne gère pas non plus la notion de *séries*.

```
python -m training.projects.mediamanager.mediamanager web
```

lance le serveur web pour l'application Flask qui est connecté à la base de données.

## Cahiers d'exercices

Le répertoire *workbooks* contient des *cahiers d'exercices*. Ceux-ci sont
des documents type *Jupyter Notebooks* générés à l'aide de
[Jupyter](http://jupyter.org/). Ce dernier est inclus dans les dépendances.
 
Dans un terminal localisé dans le répertoire racine du projet,  exécutez la
commande

```
python -m jupyter notebook
```

Vous pouvez maintenant travailler avec les *workbooks*. Ceux-ci sont proposés
comme outil pour vous aider à vous familiariser avec le langage.

## Les autres répertoires
Le répertoire `/docs` contient normalement une documentation du projet. Elle
contient actuellement un exemple de contenu pouvant produire un support pour
cette formation. Notez que comme toute bonne documentation… elle n'est pas
maintenue.
 
Le répertoire `/draft` est un répertoire contenant des squelettes de modules à
compléter.

## Dépendances du projet
Le fichier requirements liste les dépendances nécessaires au projet dans son
ensemble. Il s'agit de :
 * [bottle](https://bottlepy.org/) : microframework web utilisé lorsque le thème
 du web est abordé.
 * [coverage](http://flask.pocoo.org/) : framework permettant de générer les
 métriques de couverture du code.
 * [Faker](https://faker.readthedocs.io/) : lib permettant de générer des
 données
 * [Flask](http://flask.pocoo.org/) : microframework web utilisé lorsque le
 thème du web est abordé.
 * [ipython](https://ipython.org/) : remplaçant du shell interractif.
 * [pylint](https://www.pylint.org/) : outil d'analyse de qualité du code.
 * [pytest](https://docs.pytest.org/) : lib de tests unitaires, à utiliser de
 préférence par rapport à unittest.
 * [Sphinx](http://www.sphinx-doc.org/) : outil de génération de documentation.

## Ressources

Le répertoire *assets* contient des fichiers issus de plusieurs sources
publiques, les droits appartenant à leur propriétaires respectifs :
 * L'[Opendata de la SNCF](https://data.sncf.com/)
 * L'[Opendata du Ministère de la Culture](https://data.culture.gouv.fr/pages/home/)

Les documents contenus dans ces répertoires permettent de travailler sur des
volumes important de données.

Durant la formation, des ressources complémentaires peuvent être disponibles
[sur le partage suivant](https://goo.gl/lRyzMZ).
