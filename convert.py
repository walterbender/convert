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

lenght = {'m': (1, 1), 'km': (1000, 0.001), 'cm': (0.01, 100),
          'mm': (0.001, 100), 'dm': (0.1, 10), 'dam': (10, 0.1),
          'hm': (100, 0.01)}

speed = {'Km/H': (1, 1)}

area = {'Meter2': (1, 1)}

weight = {'Gram': (1, 1)}

volume = {'Meter3': (1, 1)}

temp = {'Celsius': (1, 1)}


def convert(number, unit, to_unit, dic):
    main_unit = number * dic[unit][0]
    return main_unit * dic[to_unit][1]
