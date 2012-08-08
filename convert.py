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


lenght = {'Meter': 1, 'Kilometer': 0.001, 'Centimeter': 0.01, 'Yard': 1.09361,
          'Foot': 3.28084, 'Fathoms': 0.5468, 'mm': 0.001, 'dm': 0.1, 'dam': 10,
          'hm': 100}

speed = {'Km/H': 1}

area = {'Meter2': 1, 'Kilometer2': 0.001, 'Centimeter2': 100, 'Yard2': 1.09361,
        'Foot2': 3.28084, 'Fathoms2': 0.5468, 'mm2': 1000, 'dm2': 10,
        'dam2': 0.1, 'hm2': 0.01}

weight = {'Gram': 1, 'hg': 0.01, 'dag': 0.1, 'dg': 10, 'cg': 100, 'mg': 1000,
          'Kilogram': 1000}

volume = {'Meter3': 1, 'Kilometer3': 0.001, 'Centimeter3': 100,
          'Yard3': 1.09361, 'Foot3': 3.28084, 'Fathoms3': 0.5468, 'mm3': 1000,
          'dm3': 10, 'dam3': 0.1, 'hm3': 0.01, 'Liter': 1, 'Kiloliter': 0.001,
          'Centiliter': 100, 'ml': 1000, 'dl': 10, 'dal': 0.1, 'hl': 0.01}


temp = {'Celsius': 1}

dic = lenght


def convert(number, unit, to_unit):
    return number * dic[unit] * dic[to_unit]


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
