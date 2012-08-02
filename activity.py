#!/usr/bin/env python
# -*- coding: utf-8 -*-

# activity.py by:
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

import gtk
import pango

from sugar.activity import activity
from sugar.activity.widgets import StopButton
from sugar.activity.widgets import ActivityToolbarButton
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.graphics.radiotoolbutton import RadioToolButton


lenght = {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Yard": 1.09361,
          "Foot": 3.28084, "Fathoms": 0.5468}
speed = {"Km/H": 1}
area = {"M2": 1}
weight = {"Gram": 1, "Kilogram": 1000}
volume = {"M3": 1}
time = {"Hour": 1}
temp = {"Celsius": 1}


class ConvertActivity(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle, True)

        self.dic = {}

        #Canvas
        self.canvas = gtk.VBox()

        self.set_canvas(self.canvas)

        hbox = gtk.HBox()
        self.canvas.pack_start(hbox, False, padding=5)
        self.combo1 = gtk.combo_box_new_text()
        self.combo1.connect('changed', lambda w: self._update_label())
        hbox.pack_start(self.combo1, False, True, 20)

        flip_btn = gtk.Button()
        flip_btn.add(gtk.image_new_from_file("icons/flip.svg"))
        flip_btn.connect('clicked', self._flip)
        hbox.pack_start(flip_btn, True, False)

        self.combo2 = gtk.combo_box_new_text()
        self.combo2.connect('changed', lambda w: self._update_label())
        hbox.pack_end(self.combo2, False, True, 20)

        adjustment = gtk.Adjustment(1.0, 0.1, 1000000, 0.1, 0.1, 0.1)
        spin_box = gtk.HBox()
        self.spin_btn = gtk.SpinButton(adjustment, 1.0, 1)
        self.spin_btn.connect("value-changed", lambda w: self._update_label())
        spin_box.pack_start(self.spin_btn, True, False)
        self.canvas.pack_start(spin_box, False, False, 5)

        scroll = gtk.ScrolledWindow()
        scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.label = gtk.Label()
        self.label.set_text("%s ~ %s" % (str(self.spin_btn.get_value()),
                            str(self.spin_btn.get_value())))
        self.label.modify_font(pango.FontDescription('60'))
        scroll.add_with_viewport(self.label)
        self.canvas.add(scroll)
        self.label_info = gtk.Label("   Convert \n000 x 000 = 000")
        self.label_info.modify_font(pango.FontDescription('12'))
        self.canvas.pack_end(self.label_info, 0, True, 30)

        #Toolbar
        toolbarbox = ToolbarBox()

        activity_button = ActivityToolbarButton(self)

        toolbarbox.toolbar.insert(activity_button, 0)

        separator = gtk.SeparatorToolItem()
        separator.set_expand(False)
        separator.set_draw(True)
        toolbarbox.toolbar.insert(separator, -1)

        # RadioToolButton
        self._lenght_btn = RadioToolButton()
        self._lenght_btn.connect("clicked",
                                 lambda w: self._update_combo(lenght))
        self._lenght_btn.set_tooltip("Lenght")
        self._lenght_btn.props.icon_name = "lenght"

        self._volume_btn = RadioToolButton()
        self._volume_btn.connect("clicked",
                                 lambda w: self._update_combo(volume))
        self._volume_btn.set_tooltip("Volume")
        self._volume_btn.props.icon_name = "volume"
        self._volume_btn.props.group = self._lenght_btn

        self._area_btn = RadioToolButton()
        self._area_btn.connect("clicked",
                               lambda w: self._update_combo(area))
        self._area_btn.set_tooltip("Area")
        self._area_btn.props.icon_name = "area"
        self._area_btn.props.group = self._lenght_btn

        self._weight_btn = RadioToolButton()
        self._weight_btn.connect("clicked",
                                 lambda w: self._update_combo(weight))
        self._weight_btn.set_tooltip("Weight")
        self._weight_btn.props.icon_name = "weight"
        self._weight_btn.props.group = self._lenght_btn

        self._speed_btn = RadioToolButton()
        self._speed_btn.connect("clicked",
                                lambda w: self._update_combo(speed))
        self._speed_btn.set_tooltip("Speed")
        self._speed_btn.props.icon_name = "speed"
        self._speed_btn.props.group = self._lenght_btn

        self._time_btn = RadioToolButton()
        self._time_btn.connect("clicked",
                               lambda w: self._update_combo(time))
        self._time_btn.set_tooltip("Time")
        self._time_btn.props.icon_name = "time"
        self._time_btn.props.group = self._lenght_btn

        self._temp_btn = RadioToolButton()
        self._temp_btn.connect("clicked",
                               lambda w: self._update_combo(temp))
        self._temp_btn.set_tooltip("Temperature")
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
        self._update_combo(lenght)
        self.show_all()

    def _update_label(self):
        self.label.set_text("%s ~ %s" % (str(self.spin_btn.get_value()),
                            str(self._convert())))

    def _update_combo(self, data):
        for x in self.dic.keys():
            self.combo1.remove_text(0)
            self.combo2.remove_text(0)
        self.dic = data
        for x in self.dic.keys():
            self.combo1.append_text(x)
            self.combo2.append_text(x)
        self.combo1.set_active(0)
        self.combo2.set_active(0)
        self.show_all()
        self._update_label()

    def _get_active_text(self, combobox):
        model = combobox.get_model()
        active = combobox.get_active()
        if active < 0:
            return None
        return model[active][0]

    #idea para cambiar los valores de los combos
    def _flip(self, widget):
        active_combo1 = self.combo1.get_active()
        active_combo2 = self.combo2.get_active()
        self.combo1.set_active(active_combo2)
        self.combo2.set_active(active_combo1)
        self.spin_btn.set_value(float(self.label.get_text().split(' ~ ')[1]))
        self._update_label()

    def _update_label_info(self, igual=False, text1=None, text2=None):
        if igual:
            value = 1
        else:
            value = round(self.dic[text1] * self.dic[text2], 2)
        self.label_info.set_text("   Convert \n %s x %s = %s" % (str(text1),
                                 str(value), str(text2)))

    def _convert(self):
        number = self.spin_btn.get_value()
        unit = self._get_active_text(self.combo1)
        to_unit = self._get_active_text(self.combo2)
        if unit == to_unit:
            self._update_label_info(igual=True, text1=unit, text2=to_unit)
            return self._round(number)
        else:
            self._update_label_info(igual=False, text1=unit, text2=to_unit)
            return self._round(number * self.dic[unit] * self.dic[to_unit])

    def _round(self, num):
        num = str(num)
        before_dot = num.split(".")[0]
        then_dot = num.split(".")[1]

        short_num = before_dot + "." + then_dot[:2]
        print short_num

        return float(short_num)

#    def _set_size(self):
#
