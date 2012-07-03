#!/usr/bin/env python
# -*- coding: utf-8 -*-

# comverter.py by:
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
# adic_long with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

dic = {}

dic_long = {"Metro": 1, "Yarda": 1.09361, "Pie": 3.28084, "Brazas": 0.5468}
vol = {}
area = {}
peso = {}
vel = {}
time = {}

def convert(number, uni1, uni2, type_u):
    if type_u == "dic_long":
        dic = dic_long
    elif type_u == "vol":
        dic = vol
    elif type_u == "area":
        dic = area
    elif type_u == "peso":
        dic = peso
    elif type_u == "vel":
        dic = vel
    elif type_u == "time":
        dic = time

    unidad = number * dic[uni1]

    return unidad * dic[uni2]

def return_list(type_u):
    if type_u == "dic_long":
        dic = dic_long
    elif type_u == "vol":
        dic = vol
    elif type_u == "area":
        dic = area
    elif type_u == "peso":
        dic = peso
    elif type_u == "vel":
        dic = vel
    elif type_u == "time":
        dic = time

    return dic.key()
