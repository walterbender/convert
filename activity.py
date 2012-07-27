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
import pango

from sugar.activity import activity
from sugar.activity.widgets import StopButton
from sugar.activity.widgets import ActivityToolbarButton
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.graphics.radiotoolbutton import RadioToolButton


lenght = {"Metro": 1, "Km": 1000, "cm": 0.01, "Yarda": 1.09361, "Pie": 3.28084,
          "Brazas": 0.5468}
speed = {"km/hs": 1}
area = {"m2": 1}
weight = {"g": 1, "Kg": 1000}
volume = {"m3": 1}
time = {"hs": 1}
temp = {"C": 1}


class ConvertActivity(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle, True)

        self.dic = {}

        toolbarbox = ToolbarBox()

        activity_button = ActivityToolbarButton(self)

        toolbarbox.toolbar.insert(activity_button, 0)

        separator = gtk.SeparatorToolItem()
        separator.set_expand(False)
        separator.set_draw(True)
        toolbarbox.toolbar.insert(separator, -1)

        # RadioToolButton
        self._lenght_btn = RadioToolButton()
        self._lenght_btn.connect("clicked", lambda w: self.update_combo(lenght))
        self._lenght_btn.set_tooltip("lenght")
        self._lenght_btn.props.icon_name = "lenght"

        self._volume_btn = RadioToolButton()
        self._volume_btn.connect("clicked", lambda w: self.update_combo(volume))
        self._volume_btn.set_tooltip("volume")
        self._volume_btn.props.icon_name = "volume"
        self._volume_btn.props.group = self._lenght_btn

        self._area_btn = RadioToolButton()
        self._area_btn.connect("clicked", lambda w: self.update_combo(area))
        self._area_btn.set_tooltip("area")
        self._area_btn.props.icon_name = "area"
        self._area_btn.props.group = self._lenght_btn

        self._weight_btn = RadioToolButton()
        self._weight_btn.connect("clicked", lambda w: self.update_combo(weight))
        self._weight_btn.set_tooltip("weight")
        self._weight_btn.props.icon_name = "weight"
        self._weight_btn.props.group = self._lenght_btn

        self._speed_btn = RadioToolButton()
        self._speed_btn.connect("clicked", lambda w: self.update_combo(speed))
        self._speed_btn.set_tooltip("speed")
        self._speed_btn.props.icon_name = "speed"
        self._speed_btn.props.group = self._lenght_btn

        self._time_btn = RadioToolButton()
        self._time_btn.connect("clicked", lambda w: self.update_combo(time))
        self._time_btn.set_tooltip("time")
        self._time_btn.props.icon_name = "time"
        self._time_btn.props.group = self._lenght_btn

        self._temp_btn = RadioToolButton()
        self._temp_btn.connect("clicked", lambda w: self.update_combo(temp))
        self._temp_btn.set_tooltip("temperature")
        self._temp_btn.props.icon_name = "temp"
        self._temp_btn.props.group = self._lenght_btn

        toolbarbox.toolbar.insert(self._lenght_btn, -1)
        toolbarbox.toolbar.insert(self._volume_btn, -1)
        toolbarbox.toolbar.insert(self._area_btn, -1)
        toolbarbox.toolbar.insert(self._weight_btn, -1)
        toolbarbox.toolbar.insert(self._speed_btn, -1)
        toolbarbox.toolbar.insert(self._time_btn, -1)
        toolbarbox.toolbar.insert(self._temp_btn, -1)

        #
        separator = gtk.SeparatorToolItem()
        separator.set_expand(True)
        separator.set_draw(False)
        toolbarbox.toolbar.insert(separator, -1)

        stopbtn = StopButton(self)
        toolbarbox.toolbar.insert(stopbtn, -1)

        self.set_toolbar_box(toolbarbox)

        #Canvas
        self.canvas = gtk.VBox()

        self.set_canvas(self.canvas)

        hbox = gtk.HBox()
        self.canvas.pack_start(hbox, False, padding=5)
        self.combo1 = gtk.combo_box_new_text()
        hbox.pack_start(self.combo1, False, True, 2)

        flip_btn = gtk.Button()
        flip_image = gtk.Image()
        flip_image.set_from_file("to.svg")
        flip_btn.add(flip_image)
        hbox.pack_start(flip_btn, True, False)

        self.combo2 = gtk.combo_box_new_text()
        hbox.pack_end(self.combo2, False, True, 2)

        adjustment = gtk.Adjustment(1.0, 0.1, 1000, 0.1, 0.1, 0.1)
        spin_box = gtk.HBox()
        self.spin_btn = gtk.SpinButton(adjustment, 1.0, 1)
        self.spin_btn.connect("button-press-event", self.update_label)
        spin_box.pack_start(self.spin_btn, True, False)
        self.canvas.pack_start(spin_box, False, False, 5)

        self.label = gtk.Label()
        self.label.set_text("%s ~ %s" % (str(self.spin_btn.get_value()),
                            str(self.spin_btn.get_value())))
        self.label.modify_font(pango.FontDescription('80'))
        self.canvas.pack_start(self.label, True, True, 5)

        label_info = gtk.Label("   Convert \n000 x 000 = 000")
        self.canvas.pack_start(label_info, True, True, 5)

        #self.dic = lenght
        self.show_all()

    def update_label(self, widget, data=None):
        self.label.set_text("%s ~ %s" % (str(self.spin_btn.get_value()),
                            self.convert()))

    def update_combo(self, data):
        for x in self.dic.keys():
            print x
            self.combo1.remove_text(0)
            self.combo2.remove_text(0)
        self.dic = data
        for x in self.dic.keys():
            self.combo1.append_text(x)
            self.combo2.append_text(x)
        self.show_all()

    def get_active_text(self, combobox):
        model = combobox.get_model()
        active = combobox.get_active()
        if active < 0:
            return None
        return model[active][0]

    def convert(self):
        _number = self.spin_btn.get_value()
        _unit = self.get_active_text(self.combo1)
        _to_unit = self.get_active_text(self.combo2)
        _value = _number * self.dic[_unit]
        return _value * self.dic[_to_unit]
