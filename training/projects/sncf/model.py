"""
Work in progress pour modèle objet du comptage transilien
"""

import datetime as dt


def date_from_sncf_file(day: str):
    return dt.datetime.strptime(day, '%Y-%m-%d')


class Station:
    def __init__(self, id: int, name: str):
        self._id = id
        self._name = name
        self._counts = []

    @property
    def id(self):
        return self._id

    @property
    def _name(self):
        return self._name

    def add_count(self, day: dt.datetime, hour: str, line: str, count: int):
        count = Count(day, hour, line, count)
        if count in self._counts:
            raise ValueError(f"Count dor day {day}, {hour}, {line} exist")

        self._counts.append(count)


class Count:
    def __init__(self, day: dt.datetime, hour: str, line: str, count: int):
        self.day = day
        self.hour = hour
        self.line = line
        self.count = count

    def __eq__(self, other):
        if not isinstance(other, Count):
            return False

        return (self.day, self.line, self.hour) == (other.day, other.line, other.hour)
