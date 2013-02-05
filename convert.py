# Copyright (C) 2012 Cristhofer Travieso <cristhofert97@gmail.com>

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

from gettext import gettext as _

length = {_('Meters (m)'): (1, 1),
          _('Kilometers (km)'): (1000, 0.001),
          _('Centimeter (cm)'): (0.01, 100),
          _('Cables'): (185.0, 0.00540540540541),
          _('Miles'): (1609.344, 0.000621371192237),
          _('Millimeters (mm)'): (0.001, 1000),
          _('Decimeter (dm)'): (0.1, 10),
          _('Decameter'): (10, 0.1),
          _('Hectometers (hm)'): (100, 0.01),
          _('Chains'): (20.1, 0.0497512437811),
          _('Ell'): (1.14, 0.877192982456),
          _('Ems (Pica)'): (0.00422, 236.966824645),
          _('Fathoms'): (1.83, 0.546448087432),
          _('feet'): (0.3048, 3.280839895013123),
          _('Furlongs'): (201.0, 0.00497512437811),
          _('Inches (in)'): (0.0254, 39.3700787402),
          _('Micrometers'): (0.000001, 1000000.0),
          _('Scandinavian mile'): (10000, 0.0001),
          _('Yards'): (0.914, 1.09409190372)
          }

area = {_('Meter'): (1, 1, 2),
        _('feet'): (0.092903, 10.763915051182416, 2),
        _('Yard'): (0.836127, 1.1959905612424908, 2),
        _('Inch'): (0.00064516, 1550.0031000062002, 2),
        _('Kilometer'): (1000000, 0.000001, 2),
        _('Mile'): (2589990, 3.8610187684122333e-7, 2),
        _('Centimeter'): (0.0001, 10000, 2),
        _('Millimeter'): (0.000001, 1000000, 2),
        _('Micrometer'): (1e-12, 1000000000000, 2),
        _('Acre'): (4046.86, 0.00024710516301527604)
        }

weight = {_('Gram'): (1, 1),
          _('Kilogram'): (1000, 0.001),
          _('Milligram'): (0.001, 1000.0000000000001),
          _('Ton'): (1000000, 0.000001),
          _('Pound'): (453.592, 0.0022046244201837776),
          _('Ounce'): (28.3495, 0.03527399072294044),
          _('Carat'): (0.2, 5)
          }

volume = {_('Meter'): (1, 1, 3),
          _('feet'): (0.0283168, 35.31472482766414, 3),
          _('Yard'): (0.764555, 1.307950376362721, 3),
          _('Inch'): (0.0000163871, 61023.61003472243, 3),
          _('Kilometer'): (1000000000, 1e-9, 3),
          _('Mile'): (4168180000, 2.399128636479231e-10, 3),
          _('Centimeter'): (0.000001, 1000000, 3),
          _('Millimeter'): (1e-9, 999999999.9999999, 3),
          _('Liter'): (0.001, 1000),
          _('Milliliter'): (0.000001, 1000000, 3),
          _('Pint'): (0.000473176, 2113.378531455526),
          _('Quart'): (0.000946353, 1056.6881491367385),
          _('Gallon'): (0.00378541, 264.172176857989)
          }

speed = {_('Kilometers/Hour'): (1, 1),
         _('Centimeters/Minute'): (0.000679856115108, 1470.8994709),
         _('Centimeters/Second'): (0.0359712230216, 27.8),
         _('feet/Hour'): (0.000304676258993, 3282.17237308),
         _('Feet/Minute'): (0.018273381295, 54.7244094488),
         _('Feet/Second'): (1.09712230216, 0.911475409836),
         _('Inches/Second'): (0.0913669064748, 10.9448818898),
         _('Kilometers/Second'): (3597.12230216, 0.000278),
         _('Knots'): (1.84892086331, 0.540856031128),
         _('Mach'): (1194.24460432, 0.00083734939759),
         _('Meters/Second'): (3.59712230216, 0.278),
         }

time = {_('Day'): (1, 1),
        _('Week'): (7, 0.14285714285714285),
        _('Month'): (30.4375, 0.03285420944558522),
        _('Year'): (365.25, 0.0027378507871321013),
        _('Hour'): (0.041666666666666664, 24),
        _('Minute'): (0.0006944444444444445, 1440),
        _('Second'): (0.000011574074074074073, 86400),
        _('Millisecond'): (1.1574074074074074e-8, 86400000),
        _('Microsecond'): (1.1574074074074074e-11, 86400000000),
        _('Nanosecond'): (1.1574074074074075e-14, 86400000000000),
        _('Picosecond'): (1.1574074074074074e-17, 86400000000000000),
        }

temp = {_('Celsius'): (1, 1),
        _('Kelvin'): (274.15, -272.15),
        _('Fahrenheit'): (-17.22222222222222, 33.8)}



def convert(number, unit, to_unit, dic):
    if dic == temp:
        if unit == to_unit:
            return number
        elif unit == 'Celsius' and to_unit == 'Kelvin':
            return number + 273.15
        elif unit == 'Kelvin' and to_unit == 'Celsius':
            return number - 273.15
        elif unit == 'Celsius' and to_unit == 'Fahrenheit':
            return 1.8 * number + 32
        elif unit == 'Fahrenheit' and to_unit == 'Celsius':
            return (number - 32) / 1.8
        elif unit == 'Kelvin' and to_unit == 'Fahrenheit':
            return 9/5 * number - 459.67
        elif unit == 'Fahrenheit' and to_unit == 'Kelvin':
            return (number + 459.67) / 1.8
        else:
            pass
    else:
        main_unit = number * dic[unit][0]
        return main_unit * dic[to_unit][1]
