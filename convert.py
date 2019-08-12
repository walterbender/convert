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
import math

length = {
    # TRANS: https://en.wikipedia.org/wiki/Metre
    _('Meters (m)'): (1, 1),  # SI UNIT
    # TRANS: https://en.wikipedia.org/wiki/Kilometre
    _('Kilometers (km)'): (1000, 0.001),
    # TRANS: https://en.wikipedia.org/wiki/Centimetre
    _('Centimeter (cm)'): (0.01, 100),
    # TRANS: https://en.wikipedia.org/wiki/Cable_length
    _('Cables'): (185.0, 0.00540540540541),
    # TRANS: https://en.wikipedia.org/wiki/Mile
    _('Miles'): (1609.344, 0.000621371192237),
    # TRANS: https://en.wikipedia.org/wiki/Millimetre
    _('Millimeters (mm)'): (0.001, 1000),
    # TRANS: https://en.wikipedia.org/wiki/Decimetre
    _('Decimeter (dm)'): (0.1, 10),
    # TRANS: https://en.wikipedia.org/wiki/Decametre
    _('Decameter'): (10, 0.1),
    # TRANS: https://en.wikipedia.org/wiki/Hectometre
    _('Hectometers (hm)'): (100, 0.01),
    # TRANS: https://en.wikipedia.org/wiki/Chain_(unit)
    _('Chains'): (20.1, 0.0497512437811),
    # TRANS: https://en.wikipedia.org/wiki/Ell
    _('Ell'): (1.14, 0.877192982456),
    # TRANS: https://en.wikipedia.org/wiki/Em_(typography)
    _('Ems (Pica)'): (0.00422, 236.966824645),
    # TRANS: https://en.wikipedia.org/wiki/Fathom
    _('Fathoms'): (1.83, 0.546448087432),
    # TRANS: https://en.wikipedia.org/wiki/Foot_(unit)
    _('feet'): (0.3048, 3.280839895013123),
    # TRANS: https://en.wikipedia.org/wiki/Furlong
    _('Furlongs'): (201.0, 0.00497512437811),
    # TRANS: https://en.wikipedia.org/wiki/Inch
    _('Inches (in)'): (0.0254, 39.3700787402),
    # TRANS: https://en.wikipedia.org/wiki/Micrometre
    _('Micrometers'): (0.000001, 1000000.0),
    # TRANS: https://en.wikipedia.org/wiki/Scandinavian_mile
    _('Scandinavian mile'): (10000, 0.0001),
    # TRANS: https://en.wikipedia.org/wiki/Yard
    _('Yards'): (0.914, 1.09409190372),
}

area = {
    # TRANS: https://en.wikipedia.org/wiki/Metre
    _('Square Meter'): (1, 1, 2),  # SI UNIT
    _('Square feet'): (0.092903, 10.763915051182416, 2),
    # TRANS: https://en.wikipedia.org/wiki/Yard
    _('Square Yard'): (0.836127, 1.1959905612424908, 2),
    # TRANS: https://en.wikipedia.org/wiki/Inch
    _('Square Inch'): (0.00064516, 1550.0031000062002, 2),
    # TRANS: https://en.wikipedia.org/wiki/Kilometre
    _('Square Kilometer'): (1000000, 0.000001, 2),
    # TRANS: https://en.wikipedia.org/wiki/Mile
    _('Square Mile'): (2589990, 3.8610187684122333e-7, 2),
    # TRANS: https://en.wikipedia.org/wiki/Centimetre
    _('Square Centimeter'): (0.0001, 10000, 2),
    # TRANS: https://en.wikipedia.org/wiki/Millimetre
    _('Square Millimeter'): (0.000001, 1000000, 2),
    # TRANS: https://en.wikipedia.org/wiki/Micrometre
    _('Square Micrometer'): (1e-12, 1000000000000, 2),
    # TRANS: https://en.wikipedia.org/wiki/Acre
    _('Acre'): (4046.86, 0.00024710516301527604),
}

weight = {
    # TRANS: https://en.wikipedia.org/wiki/Gram
    _('Gram'): (1, 1),
    # TRANS: https://en.wikipedia.org/wiki/Kilogram
    _('Kilogram'): (1000, 0.001),  # SI UNIT
    # TRANS: https://en.wikipedia.org/wiki/Kilogram#SI_multiples
    _('Milligram'): (0.001, 1000.0000000000001),
    # TRANS: https://en.wikipedia.org/wiki/Ton
    _('Ton'): (1000000, 0.000001),
    # TRANS: https://en.wikipedia.org/wiki/Pound_(mass)
    _('Pound'): (453.592, 0.0022046244201837776),
    # TRANS: https://en.wikipedia.org/wiki/Ounce
    _('Ounce'): (28.3495, 0.03527399072294044),
    # TRANS: https://en.wikipedia.org/wiki/Carat_(mass)
    _('Carat'): (0.2, 5),
}

volume = {
    _('Cubic Meter'): (1, 1, 3),  # SI UNIT
    _('Cubic feet'): (0.0283168, 35.31472482766414, 3),
    _('Cubic Yard'): (0.764555, 1.307950376362721, 3),
    _('Cubic Inch'): (0.0000163871, 61023.61003472243, 3),
    _('Cubic Kilometer'): (1000000000, 1e-9, 3),
    _('Cubic Mile'): (4168180000, 2.399128636479231e-10, 3),
    _('Cubic Centimeter'): (0.000001, 1000000, 3),
    _('Cubic Millimeter'): (1e-9, 999999999.9999999, 3),
    # TRANS: https://en.wikipedia.org/wiki/Litre
    _('Liter'): (0.001, 1000),
    # TRANS: https://en.wikipedia.org/wiki/Litre
    _('Milliliter'): (0.000001, 1000000),  # Its only mililitre not cube.
    # TRANS: https://en.wikipedia.org/wiki/Pint
    _('Pint'): (0.000473176, 2113.378531455526),
    # TRANS: https://en.wikipedia.org/wiki/Quart
    _('Quart'): (0.000946353, 1056.6881491367385),
    # TRANS: https://en.wikipedia.org/wiki/Gallon
    _('Gallon'): (0.00378541, 264.172176857989),
}

speed = {
    # TRANS: https://en.wikipedia.org/wiki/Kilometres_per_hour
    _('Kilometers/Hour'): (1, 1),
    _('Centimeters/Minute'): (0.000679856115108, 1470.8994709),
    _('Centimeters/Second'): (0.0359712230216, 27.8),
    _('feet/Hour'): (0.000304676258993, 3282.17237308),
    _('Feet/Minute'): (0.018273381295, 54.7244094488),
    # TRANS: https://en.wikipedia.org/wiki/Foot_per_second
    _('Feet/Second'): (1.09712230216, 0.911475409836),
    # TRANS: https://en.wikipedia.org/wiki/Inch_per_second
    _('Inches/Second'): (0.0913669064748, 10.9448818898),
    _('Kilometers/Second'): (3597.12230216, 0.000278),
    # TRANS: https://en.wikipedia.org/wiki/Knot_(unit)
    _('Knots'): (1.84892086331, 0.540856031128),
    # TRANS: https://en.wikipedia.org/wiki/Mach_number
    _('Mach'): (1194.24460432, 0.00083734939759),
    # TRANS: https://en.wikipedia.org/wiki/Metre_per_second
    _('Meters/Second'): (3.59712230216, 0.278),  # SI UNIT
}

time = {
    # TRANS: https://en.wikipedia.org/wiki/Day
    _('Day'): (1, 1),
    # TRANS: https://en.wikipedia.org/wiki/Week
    _('Week'): (7, 0.14285714285714285),
    # TRANS: https://en.wikipedia.org/wiki/Month
    _('Month'): (30.4375, 0.03285420944558522),
    # TRANS: https://en.wikipedia.org/wiki/Year
    _('Year'): (365.25, 0.0027378507871321013),
    # TRANS: https://en.wikipedia.org/wiki/Hour
    _('Hour'): (0.041666666666666664, 24),
    # TRANS: https://en.wikipedia.org/wiki/Minute
    _('Minute'): (0.0006944444444444445, 1440),
    # TRANS: https://en.wikipedia.org/wiki/Second
    _('Second'): (0.000011574074074074073, 86400),  # SI UNIT
    # TRANS: https://en.wikipedia.org/wiki/Millisecond
    _('Millisecond'): (1.1574074074074074e-8, 86400000),
    # TRANS: https://en.wikipedia.org/wiki/Microsecond
    _('Microsecond'): (1.1574074074074074e-11, 86400000000),
    # TRANS: https://en.wikipedia.org/wiki/Nanosecond
    _('Nanosecond'): (1.1574074074074075e-14, 86400000000000),
    # TRANS: https://en.wikipedia.org/wiki/Picosecond
    _('Picosecond'): (1.1574074074074074e-17, 86400000000000000),
}

temp = {
    # TRANS: https://en.wikipedia.org/wiki/Celsius
    _('Celsius'): (1, 1),
    # TRANS: https://en.wikipedia.org/wiki/Kelvin
    _('Kelvin'): (274.15, -272.15),  # SI UNIT
    # TRANS: https://en.wikipedia.org/wiki/Fahrenheit
    _('Fahrenheit'): (-17.22222222222222, 33.8),
}

circle = {
    _('Degrees'): (1, 1),
    _('Radians'): (0.0174533, 57.2958),
}

pressure = {
    _('Pascal (Pa)'): (1, 1),  # SI unit
    _('Bar'): (100000, 1e-5),
    _('Atmosphere (atm)'): (101325, 9.869232667e-6),
    _('Torr'): (133.322, 7.500637554192e-3),
    _('Pounds per square inch (psi)'): (6894.76, 1.45037680789e-4),
}

force = {
    _('Newton (N)'): (1, 1),  # SI UNIT
    _('Dyne (dyn)'): (1e-5, 100000),
    _('Poundal (pdl)'): (0.138255028, 7.233009999462732),
    _('Kilogram-force (kp)'): (9.80665, 0.101971621297793),
}

energy = {
    _('Joules (J)'): (1, 1),  # SI unit
    _('KiloJoule (KJ)'): (1000, 1e-3),
    _('Calories (cal)'): (4.184, 0.239005736137667),
    _('KiloCalories (KCal)'): (4184, 0.000239005736138),
    _('Watt hour'): (3600, 2.7777777777e-4),
    _('Electronvolt (eV)'): (1.6022e-19, 6.242e18),
}

storage = {
    _('Byte'): (1, 1),  # SI UNIT
    _('Bit'): (0.125, 8),
    _('Kilobyte (KB)'): (1e3, 1e-3),
    _('Megabyte (MB)'): (1e6, 1e-6),
    _('Gigabyte (GB)'): (1e9, 1e-9),
    _('Terabyte (TB)'): (1e12, 1e-12),
    _('Petabyte (PB)'): (1e15, 1e-15),
}


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
            return 9 / 5 * number - 459.67
        elif unit == 'Fahrenheit' and to_unit == 'Kelvin':
            return (number + 459.67) / 1.8
        else:
            pass
    elif dic == circle:
        if unit == to_unit:
            return number
        elif unit == 'Radians':
            return math.degrees(number)
        elif unit == 'Degrees':
            return math.radians(number)
        else:
            pass
    else:
        if unit == to_unit:
            return number
        else:
            main_unit = number * dic[unit][0]
            return main_unit * dic[to_unit][1]
