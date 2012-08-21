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
          'Barleycorns': (0.00847, 118.063754427),
          'Cables': (185.0, 0.00540540540541),
          'Milimeters[mm]': (0.001, 1000), 'Decimeter[dm]': (0.1, 10),
          'Decameter': (10, 0.1),
          'Hectometers[cm]': (100, 0.01),
          'Chains': (20.1, 0.0497512437811), 'Ell': (1.14, 0.877192982456),
          'Ems(pica)': (0.00422, 236.966824645),
          'Fathoms': (1.83, 0.546448087432),
          'Foot': (0.3048, 3.280839895013123),
          'Furlongs': (201.0, 0.00497512437811),
          'Inches[in]': (0.0254, 39.3700787402),
          'Micrometers': (0.000001, 1000000.0),
          'Miles(international)': (1610.0, 0.000621118012422),
          'Scandinavian mile': (10000, 0.0001),
          'Yards': (0.914, 1.09409190372)
          }

speed = {'Kilometers/Hour': (1, 1),
         'Centimeter/Minute': (1666.666667, 0)
         }

area = {'Meter2': (1, 1), 'Foot2': (0.092903, 10.763915051182416),
        'Yard2': (0.836127, 1.1959905612424908),
        'Inch2': (0.00064516, 1550.0031000062002),
        'Kilometer2': (1000000, 0.000001),
        'Mile2': (2589990, 3.8610187684122333e-7),
        'Centimeter2': (0.0001, 10000), 'milimeter2': (0.000001, 1000000),
        'Micrometer2': (1e-12, 1000000000000),
        'Acre': (4046.86, 0.00024710516301527604)
        }

weight = {'Gram': (1, 1), 'Kilogram': (1000, 0.001),
          'Miligram': (0.001, 1000.0000000000001), 'Ton': (1000000, 0.000001),
          'Pound': (453.592, 0.0022046244201837776),
          'Ounce': (28.3495, 0.03527399072294044), 'Carrat': (0.2, 5)
          }

volume = {'Meter3': (1, 1), 'Foot3': (0.0283168, 35.31472482766414),
          'Yard3': (0.764555, 1.307950376362721),
          'Inch3': (0.0000163871, 61023.61003472243),
          'Kilometer3': (1000000000, 1e-9),
          'Mile3': (4168180000, 2.399128636479231e-10),
          'Centimeter3': (0.000001, 1000000),
          'Milimeter': (1e-9, 999999999.9999999), 'Liter': (0.001, 1000),
          'Milliliter': (0.000001, 1000000),
          'Pint': (0.000473176, 2113.378531455526),
          'Quart': (0.000946353, 1056.6881491367385),
          'Gallon': (0.00378541, 264.172176857989)
          }

temp = {'Kelvin': (1, 1), 'Celsius': (274, -272),
        'Farenheit': (255.77777777777777, -457.6)
        }


def convert(number, unit, to_unit, dic):
    main_unit = number * dic[unit][0]
    return main_unit * dic[to_unit][1]
