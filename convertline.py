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

import os
import sys
import convert


estado = True

while estado:
    os.system('clear')
    print '*********convert*********'
    print convert.lenght.keys()
    number = input('No.: ')
    unit = raw_input('de : ')
    to_unit = raw_input('a: ')

    print convert.convert(number, unit, to_unit)
    if raw_input('Deseas salir(y/n): ') == 'y':
        sys.exit()
    else:
        estado = True
