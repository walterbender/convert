#!/usr/bin/env python
# -*- coding: utf-8 -*-

# convert.py by:
#    Cristhofer Travieso <cristhofert97@gmail.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

lenght = {'Meters[m]': (1, 1), 'Kilometers[km]': (1000, 0.001),
          'Centimeter[cm]': (0.01, 100),
          'barleycorns': (0.008467, 118.105586), 'cables': (182.88, 0.005468),
          'Milimeters[mm]': (0.001, 100), 'Decimeter[dm]': (0.1, 10),
          'dam': (10, 0.1),
          'Hectometers[cm]': (100, 0.01),
          'chains': (20.11684, 0.04971), 'ells(UK)': (0.875, 1.142857),
          'ems(pica)': (0.004233, 236.222332), 'fathoms': (1.8288, 0.546807),
          'foot': (0.3048, 3.28084), 'furlongs': (201.168, 0.004971),
          'hands': (0.1016, 9.84252), 'inches[in]': (0.0254, 39.370079),
          'Micrometers': (0.000001, 0), 'mil': (0.000025, 39370.07874),
          'miles(UK and US)': (1609.344, 0),
          'miles(nautical, UK)': (1853.184, 0.000621),
          'miles(nautical, international)': (1852, 0.00054),
          'Scandinavian mile': (10000, 0.0001),
          'thon': (0.000025, 39398.385827), 'yards': (0.9144, 1.0944)
          }

speed = {'kilometers/hour': (1, 1),
         'centimeter/minute': (1666.666667, 0)
         }

area = {'Meter2': (1, 1), 'foot2': (0.092903, 10.763915051182416),
        'yard2': (0.836127, 1.1959905612424908),
        'inch2': (0.00064516, 1550.0031000062002),
        'Kilometer2': (1000000, 0.000001),
        'mile2': (2589990, 3.8610187684122333e-7),
        'centimeter2': (0.0001, 10000), 'milimeter2': (0.000001, 1000000),
        'micrometer2': (1e-12, 1000000000000),
        'acre': (4046.86, 0.00024710516301527604)
        }

weight = {'Gram': (1, 1), 'Kilogram': (1000, 0.001),
          'miligram': (0.001, 1000.0000000000001), 'ton': (1000000, 0.000001),
          'Pound': (453.592, 0.0022046244201837776),
          'Ounce': (28.3495, 0.03527399072294044), 'carrat': (0.2, 5)
          }

volume = {'Meter3': (1, 1), 'foot3': (0.0283168, 35.31472482766414),
          'yard3': (0.764555, 1.307950376362721),
          'inch3': (0.0000163871, 61023.61003472243),
          'Kilometer3': (1000000000, 1e-9),
          'mile3': (4168180000, 2.399128636479231e-10),
          'centimeter3': (0.000001, 1000000),
          'Milimeter': (1e-9, 999999999.9999999), 'liter': (0.001, 1000),
          'milliliter': (0.000001, 1000000),
          'pint': (0.000473176, 2113.378531455526),
          'quart': (0.000946353, 1056.6881491367385),
          'gallon': (0.00378541, 264.172176857989)
          }

temp = {'Celsius': (1, 1), 'kelvin': (-272, 274),
        'farenheit': (-17.22222222222222, 33.8)
        }


def convert(number, unit, to_unit, dic):
    main_unit = number * dic[unit][0]
    return main_unit * dic[to_unit][1]
