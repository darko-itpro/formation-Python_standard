#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import pytest

from draft.media import mediamodel as mediamodel


def test_create_episode_without_season():
    episode = mediamodel.Episode("Title", 1)
    assert episode is not None

def test_create_episode_with_season():
    episode = mediamodel.Episode("Title", 1, 1)
    assert episode is not None

def test_title_accessible():
    episode = mediamodel.Episode("Title", 1)
    assert episode.title == "Title"

def test_should_not_assign_title():
    episode = mediamodel.Episode("Title", 1)
    with pytest.raises(AttributeError):
        episode.title = 'Other title'

def test_number_accessible():
    episode = mediamodel.Episode("Title", 1)
    assert episode.number == 1

def test_should_not_assign_number():
    episode = mediamodel.Episode("Title", 1)
    with pytest.raises(AttributeError):
        episode.number = 2

def test_season_accessible():
    episode = mediamodel.Episode("Title", 1, 2)
    assert episode.season_number == 2

def test_shouldnt_assign_season():
    episode = mediamodel.Episode("Title", 1)
    with pytest.raises(AttributeError):
        episode.season_number = 2

def test_without_season_should_be_none():
    episode = mediamodel.Episode("Title", 1)
    assert episode.season_number is None

def test_number_must_be_integer_compatible():
    episode = mediamodel.Episode('Title', 1)
    assert episode.number == 1
    episode = mediamodel.Episode('Title', "1")
    assert episode.number == 1
    with pytest.raises(ValueError):
        mediamodel.Episode('Title', "un")

def test_season_must_be_integer_compatible():
    episode = mediamodel.Episode('Title', 1, 2)
    assert episode.season_number == 2
    episode = mediamodel.Episode('Title', 1, "2")
    assert episode.season_number == 2
    with pytest.raises(ValueError):
        mediamodel.Episode('Title', 1, "un")

def test_title_should_be_string_or_raise_error():
    with pytest.raises(ValueError):
        mediamodel.Episode(10, 1)

def test_title_cannot_be_empty():
    with pytest.raises(ValueError):
        mediamodel.Episode('', 1)


def test_create_new_show():
    show = mediamodel.TvShow('Mr. Robot')
    assert show is not None

def test_show_name_accessible():
    show = mediamodel.TvShow('Mr. Robot')
    assert show.name == 'Mr. Robot'

def test_shouldnt_assign_name():
    show = mediamodel.TvShow('Mr. Robot')
    with pytest.raises(AttributeError):
        show.name = 'Dr. Who'


@pytest.fixture
def got_show():
    return mediamodel.TvShow('Game of Thrones')

def test_has_episodes_attr(got_show):
    assert hasattr(got_show, 'get_episodes')

def test_has_add_episode_attr(got_show):
    assert hasattr(got_show, 'add_episode')

def test_empty_show(got_show):
    assert len(got_show.get_episodes()) == 0

def test_add_episode_with_season_number(got_show):
    got_show.add_episode("Into the North", 1, 1)
    assert len(got_show.get_episodes()) == 1

def test_add_episode_without_season_number(got_show):
    got_show.add_episode("Into the North", 1)
    assert len(got_show.get_episodes()) == 1

def test_should_not_alter_episodes(got_show):
    episodes = got_show.get_episodes()
    episodes.append(mediamodel.Episode('Intruder', 2))
    assert len(got_show.get_episodes()) == 0

def test_should_not_add_same_episode(got_show):
    got_show.add_episode("Into the North", 1, 1)
    with pytest.raises(ValueError):
        got_show.add_episode('Kingslayer', 1, 1)
