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

import gtk

class Converter(gtk.VBox):

    def __init__(self):
        gtk.VBox.__init__(self)

        self._hbox = gtk.VBox()

        self.combo1 = gtk.Combo()

        self.combo2 = gtk.Combo()

        self.add(gtk.Label("Comvertir"))
        self._hbox(gtk.Label("De "))
        self._hbox.add(self.combo1)
        self._hbox.add(gtk.Label(" a "))
        self._hbox.add(self.combo2)

        self.add(self._hbox)
