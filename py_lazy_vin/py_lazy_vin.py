# -*- coding: utf-8 -*-

"""Main module."""
from random import choice
from helpers import Helpers
from hard_coded_vins import HARD_CODED_VINS

class LazyVin:
    _vin_list = ()
    _unique_identifier_length = 6

    def __init__(self):
        self._vin_list = HARD_CODED_VINS

    def get_random_dirty_vin(self):
        random_vin = choice(self._vin_list)
        return random_vin

    def get_random_clean_vin(self):
        dirty_vin = self.get_random_dirty_vin()
        # dirty_vin = ''
        clean_vin = dirty_vin[0:(len(dirty_vin) - self._unique_identifier_length)]
        random_unique_id = Helpers.get_random_number_of_length(self._unique_identifier_length)
        clean_vin += Helpers.get_number_as_string(random_unique_id)
        print(dirty_vin, clean_vin)


lazy = LazyVin()
lazy.get_random_clean_vin()
