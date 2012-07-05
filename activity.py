#!/usr/bin/env python
# -*- coding: utf-8 -*-

# activity.py by:
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
import convert

from sugar.activity import activity
from sugar.activity.widgets import StopButton
from sugar.activity.widgets import ActivityToolbarButton
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.graphics.radiotoolbutton import RadioToolButton

class ConvertActivity(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle, True)

        toolbarbox = ToolbarBox()

        activity_button = ActivityToolbarButton(self)

        toolbarbox.toolbar.insert(activity_button, 0)

        separator = gtk.SeparatorToolItem()
        separator.set_expand(False)
        separator.set_draw(True)
        toolbarbox.toolbar.insert(separator, -1)

        # RadioToolButton
        self._long_btn = RadioToolButton()
        self._long_btn.connect("clicked", self.update_combo, "lenght")
        self._long_btn.set_tooltip("lenght")
        self._long_btn.props.icon_name = "lenght"

        self._vol_btn = RadioToolButton()
        self._vol_btn.connect("clicked", self.update_combo, "volume")
        self._vol_btn.set_tooltip("volume")
        self._vol_btn.props.icon_name = "volume"
        self._vol_btn.props.group = self._long_btn

        self._area_btn = RadioToolButton()
        self._area_btn.connect("clicked", self.update_combo, "area")
        self._area_btn.set_tooltip("area")
        self._area_btn.props.icon_name = "area"
        self._area_btn.props.group = self._long_btn

        self._peso_btn = RadioToolButton()
        self._peso_btn.connect("clicked", self.update_combo, "peso")
        self._peso_btn.set_tooltip("peso")
        self._peso_btn.props.icon_name = "peso"
        self._peso_btn.props.group = self._long_btn

        self._vel_btn = RadioToolButton()
        self._vel_btn.connect("clicked", self.update_combo, "speed")
        self._vel_btn.set_tooltip("speed")
        self._vel_btn.props.icon_name = "speed"
        self._vel_btn.props.group = self._long_btn

        self._time_btn = RadioToolButton()
        self._time_btn.connect("clicked", self.update_combo, "time")
        self._time_btn.set_tooltip("time")
        self._time_btn.props.icon_name = "time"
        self._time_btn.props.group = self._long_btn

        self._temp_btn = RadioToolButton()
        self._temp_btn.connect("clicked", self.update_combo, "temp")
        self._temp_btn.props.icon_name = "temp"
        self._temp_btn.props.group = self._long_btn
        self._temp_btn.set_tooltip("temp")

        toolbarbox.toolbar.insert(self._long_btn, -1)
        toolbarbox.toolbar.insert(self._vol_btn, -1)
        toolbarbox.toolbar.insert(self._area_btn, -1)
        toolbarbox.toolbar.insert(self._peso_btn, -1)
        toolbarbox.toolbar.insert(self._vel_btn, -1)
        toolbarbox.toolbar.insert(self._time_btn, -1)

        #
        separator = gtk.SeparatorToolItem()
        separator.set_expand(True)
        separator.set_draw(False)
        toolbarbox.toolbar.insert(separator, -1)

        stopbtn = StopButton(self)
        toolbarbox.toolbar.insert(stopbtn, -1)

        self.set_toolbar_box(toolbarbox)

        #Canvas
        canvas = Canvas()

        self.set_canvas(canvas)

        self.show_all()


    def update_combo(self, widget, data):
        self.combo1.set_popdown_strings(convert.return_list(data))
        self.combo2.set_popdown_strings(convert.return_list(data))


class Canvas(gtk.VBox):
    def __init__(self):
        gtk.VBox.__init__(self)

        self.table = gtk.Table(rows=2, columns=4, homogeneous=False)
        self.pack_start(self.table, False)

        self.combo1 = gtk.ComboBox()
        self.table.attach(self.combo1, 1, 2, 0, 1)
        self.table.attach(gtk.Label("to"), 2, 3, 0, 1)
        self.combo2 = gtk.ComboBox()
        self.table.attach(self.combo2, 3, 4, 0, 1)

        adjustment = gtk.Adjustment(1.0, 0.1, 1000, 0.1, 0.1, 0.1)
        self.spin_btn1 = gtk.SpinButton(adjustment, 1.0, 1)
        self.table.attach(self.spin_btn1, 1, 2, 1, 2)

        adjustment = gtk.Adjustment(1.0, 0.1, 1000, 0.1, 0.1, 0.1)

        self.spin_btn2 = gtk.SpinButton(adjustment, 1.0, 1)
        self.table.attach(self.spin_btn2, 3, 4, 1, 2)
