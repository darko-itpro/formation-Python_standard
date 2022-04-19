#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module définissant les objets *métier* de la gestion d'une médiathèque.

Ce module illustre
"""

import dataclasses as dc


class TvShow:
    def __init__(self, name: str):
        self.name = name.capitalize()
        self._episodes = []

    @property
    def episodes(self):
        """
        Fonction déclarée pour exposer une property en tant qu'accesseur pour
        l'attribut episodes qui ne doit pas être modifié par l'exterrieur.

        :return: une copie de la liste des épisodes.
        """
        return self._episodes.copy()

    def add_episode(self, title, number, season_number, duration=None):
        """
        Ajoute un épisode à la série.

        :param title: Titre de l'épisode
        :param number: Numéro de l'épisode dans la saison
        :param season_number: Numéro de la saison de l'épisode
        :raise ValueError: si l'épisode existe déjà dans la série ou si les
        numéros ne représentent pas des nombres.
        """
        new_episode = Episode(title, int(number), int(season_number),
                              int(duration) if duration is not None else None)
        if new_episode in self._episodes:
            raise ValueError(
                f"Episode [s{season_number:02}e{number:02}-{title}]exists")

        self._episodes.append(new_episode)
        self._episodes.sort()

    def get_episodes(self, season=None):
        """
        Retourne une liste triée d'épisodes.

        Par défaut retourne tous les épisodes de la série. Si un numéro de
        saison est passé en paramètre, les épisodes sont filtrés en fonction de
        celui-ci.

        :param season: Saison selon laquelle filtrer les épisodes.
        :return: Une liste d'épisodes, vide si la série ne contient aucun
        épisode ou si elle ne contient pas d'épisode de la saison passée en
        paramètre.
        """
        if season is not None:
            season = int(season)
            return [episode
                    for episode in self.episodes
                    if episode.season_number == season]
        else:
            return self.episodes

    def __str__(self):
        return f"TV Show [{self.name}] - {len(self.episodes)} episodes"

    def __repr__(self):
        return f"TvShow({self.name})"


@dc.dataclass(eq=False, frozen=True)
class Episode:
    title: str
    number: int
    season_number: int
    duration: int = None

    def __post_init__(self):
        """
        Méthode exécutée après l'initialisation chargée ici de vérifier la
        cohérence des données.
        """
        if self.number < 0:
            raise ValueError(f"Episode number should be positive "
                             f"({self.number})")

        if self.season_number < 0:
            raise ValueError(f"Episode season number should be positive "
                             f"({self.season_number})")

        if self.duration is not None and self.duration <= 0:
            raise ValueError(f"Duration must be positive value, got "
                             f"{self.duration}")

    def __eq__(self, other):
        """
        Le critère d'égalité entre deux épisodes se limite aux numéro d'épisode
        et numéro de saison.

        :param other: L'objet avec lequel self est comparé.
        :return: Vrai si le numéro d'épisode et numéro de saison sont égaux
        sinon faux. Les autres paramètres ne sont pas pris en compte.
        """
        if not isinstance(other, Episode):
            return False

        return (self.number, self.season_number) == (other.number,
                                                     other.season_number)

    def __gt__(self, other):
        if not isinstance(other, Episode):
            raise TypeError(f"'>' not supported between instances of "
                            f"'Episode' and '{type(other)}'")

        return (self.season_number, self.number) \
            > (other.season_number, other.number)
