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

lenght = {'m': 1, 'km': 1000, 'cm': 0.01, 'mm': 0.001,
          'dm': 0.1, 'dam': 10, 'hm': 100}

speed = {'Km/H': 1}

area = {'Meter2': 1}

weight = {'Gram': 1}

volume = {'Meter3': 1}

temp = {'Celsius': 1}

dic = lenght


def convert(number, unit):
    metro = number * dic[unit]
    return str(metro) + 'm'

#    print '%s * %s * %s' % (number, dic[unit], dic[to_unit    ])
#    return number * dic[unit] * dic[to_unit]
#    x = number * 1 / dic[unit]
#    a = x * dic[to_unit] / 1
#    return a

#    print number, dic[unit], dic[to_unit]
#    return number * dic[unit] * dic[to_unit]

# 100cm  ___ 1m
# number ___ x
# x = number * 1m / 100cm
# x = number / dic[to_unit]
#1m __ 1000mm
#x ____ a
#a = x * 1000mm / 1m

#ATENCION! buscar por que en losnumeros aparese e-
#    def convert(self):
#        number = self.spin_btn.get_value()
#        unit = self._get_active_text(self.combo1)
#        to_unit = self._get_active_text(self.combo2)
#        if unit == to_unit:
#            self.update_label_info(True, unit, to_unit)
#            return self.recut(number)
#        else:
#            self.update_label_info(False, unit, to_unit)
#            return self.recut(number * self.dic[unit] * self.dic[to_unit])
#
