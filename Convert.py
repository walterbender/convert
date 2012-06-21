#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Comverter.py by:
#	Cristhofer Travieso <cristhofert97@gmail.com>

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


class convert():
    def __init__(self, number, uni1, uni2, type_u):
        super(convert, self).__init__()

        self.long = {}
        self.vol = {}
        self.area = {}
        self.peso = {}
        self.vel = {}
        self.time = {}

        if type_u == "long":
            self.dic = self.long
        elif type_u == "vol":
            self.dic = self.vol
        elif type_u == "area":
            self.dic = self.area
        elif type_u == "peso":
            self.dic = self.peso
        elif type_u == "vel":
            self.dic = self.vel
        elif type_u == "time":
            self.dic = self.time

        self.a = number * self.dic[uni1]

        return self.a * self.dic[uni2]
