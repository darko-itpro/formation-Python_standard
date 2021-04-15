#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Rappel:
PV = nRT, ici nR est considéré = 1

La formule réelle est P en Pascal, V en m3 et T en Kelvin (C + 273.15)
"""


class Container:

    ZERO_CELCIUS = 273.15

    def __init__(self, volume, temperature):
        self._volume = float(volume)
        self._temperature = float(temperature + self.ZERO_CELCIUS)
        self._pressure_max = self.pressure() * 2

    def pressure(self):
        return self._temperature/self._volume

    def _check_pressure(self):
        if self.pressure() >= self._pressure_max:
            print("stop all")

    def status(self):
        return self._volume, self._temperature, self.pressure()

    def increase_temperature_by(self, value):
        if value >= 0:
            self._temperature += value
        else:
            raise ValueError("Value should not be negative")

    def lower_temperature_by(self, value):
        if value >= 0:
            self._temperature -= value
        else:
            raise ValueError("Value should not be negative")

    def set_temperature_to(self, value):
        self._temperature = value

    def __str__(self):
        return f"Container status T:{self._temperature - self.ZERO_CELCIUS}, V:{self._volume}, P:{self.pressure():.2f}"
