#!/usr/bin/env python
# -*- coding: utf-8 -*-

# convert.py by:
#    Cristhofer Travieso <cristhofert97@gmail.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

lenght = {'Meters[m]': 1, 'Kilometers[km]': 1000,
          'Centimeter[cm]': 0.01,
          'barleycorns': 0.008467, 'cables': 182.88,
          'Milimeters[mm]': 0.001, 'Decimeter[dm]': 0.1,
          'dam': 10,
          'Hectometers[cm]': 100,
          'chains': 20.11684, 'ells(UK)': 0.875,
          'ems(pica)': 0.004233, 'fathoms': 1.8288,
          'foot': 0.3048, 'furlongs': 201.168,
          'hands': 0.1016, 'inches[in]': 0.0254,
          'Micrometers': 0.000001, 'mil': 0.000025,
          'miles(UK and US)': 1609.344,
          'miles(nautical, UK)': 1853.184,
          'miles(nautical, international)': 1852,
          'Scandinavian mile': 10000,
          'thon': 0.000025, 'yards': 0.9144,
          }

speed = {'kilometers/hour': 1,
         'centimeter/minute': 1666.666667,
         }

area = {'Meter2': 1, 'foot2': 0.092903,
        'yard2': 0.836127,
        'inch2': 0.00064516,
        'Kilometer2': 1000000,
        'mile2': 2589990,
        'centimeter2': 0.0001, 'milimeter2': 0.000001,
        'micrometer2': 1e-12,
        'acre': 4046.86
        }

weight = {'Gram': 1, 'Kilogram': 1000,
          'miligram': 0.001, 'ton': 1000000,
          'Pound': 453.592,
          'Ounce': 28.3495, 'carrat': 0.2
          }

volume = {'Meter3': 1, 'foot3': 0.0283168,
          'yard3': 0.764555,
          'inch3': 0.0000163871,
          'Kilometer3': 1000000000,
          'mile3': 4168180000,
          'centimeter3': 0.000001,
          'Milimeter': 1e-9, 'liter': 0.001,
          'milliliter': 0.000001,
          'pint': 0.000473176,
          'quart': 0.000946353,
          'gallon': 0.00378541
          }

temp = {'kelvin': 1, 'Celsius': 274,
        'farenheit': 255.77777777777777
        }


def convert(number, unit, to_unit, dic):
    main_unit = number * dic[unit]
    return main_unit / dic[to_unit]
