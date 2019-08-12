# -*- coding: utf-8 -*-
# Copyright (C) 2012 Cristhofer Travieso <cristhofert97@gmail.com>
#
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

import locale
import convert
import re

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from gi.repository import Pango
from gi.repository import Gdk

from sugar3.activity import activity
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.graphics.radiotoolbutton import RadioToolButton
from sugar3.graphics.style import FONT_SIZE, FONT_FACE

from gettext import gettext as _


class Ratio(Gtk.Label):
    def __init__(self):
        Gtk.Label.__init__(self)
        self.set_selectable(True)
        self._size = -1

    def set_text(self, text):
        Gtk.Label.set_text(self, text)
        length = len(text)
        if length == 0:
            return

        width = self.get_allocation().width
        size = (60 * width / 100) / length + int(FONT_SIZE * 1.2)
        if not size == self._size:
            self.modify_font(Pango.FontDescription(
                '%s %d' % (FONT_FACE, size)))
            self._size = size


class ConvertActivity(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle, True)

        self.max_participants = 1
        self.dic = {}

        self._liststore = Gtk.ListStore(str)
        arrow_font = Pango.FontDescription(
            '%s %d' % (FONT_FACE, int(FONT_SIZE * 1.8)))
        input_font = Pango.FontDescription(
            '%s %d' % (FONT_FACE, int(FONT_SIZE * 1.2)))

        self.from_unit = Gtk.ComboBox.new_with_model_and_entry(self._liststore)
        cell = Gtk.CellRendererText()
        self.from_unit.pack_start(cell, True)
        self.from_unit.set_entry_text_column(0)
        self.from_unit.connect('changed', self._from_changed_cb)
        self.from_unit.override_font(input_font)

        self.from_value = Gtk.Entry()
        self.from_value.set_placeholder_text("Enter value")
        self.from_value.connect('insert-text', self._insert_text_cb)
        self.from_value.connect('changed', self._from_changed_cb)
        self.from_value.override_font(input_font)

        self.to_value = Gtk.Entry()
        self.to_value.connect('insert-text', self._insert_text_cb)
        self.to_value.connect('changed', self._to_changed_cb)
        self.to_value.override_font(input_font)

        self.to_unit = Gtk.ComboBox.new_with_model_and_entry(self._liststore)
        cell = Gtk.CellRendererText()
        self.to_unit.pack_start(cell, True)
        self.to_unit.set_entry_text_column(0)
        self.to_unit.connect('changed', self._to_changed_cb)
        self.to_unit.override_font(input_font)

        self.arrow = Gtk.Label()
        self.arrow.override_font(arrow_font)
        self.arrow.set_text("→")

        self.ratio = Ratio()

        l_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        u_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.label1 = Gtk.Label()
        self.label1.set_markup('<big>From value</big>')
        u_hbox.pack_start(self.label1, True, True, 5)
        self.label2 = Gtk.Label()
        self.label2.set_markup('<big>From unit</big>')
        u_hbox.pack_start(self.label2, True, True, 20)
        self.label3 = Gtk.Label()
        self.label3.set_markup('<big>To value</big>')
        u_hbox.pack_start(self.label3, True, True, 20)
        self.label4 = Gtk.Label()
        self.label4.set_markup('<big>To unit</big>')
        u_hbox.pack_start(self.label4, True, True, 5)

        l_hbox.pack_start(self.from_value, True, True, 5)
        l_hbox.pack_start(self.from_unit, True, True, 5)
        l_hbox.pack_start(self.arrow, False, False, 15)
        l_hbox.pack_start(self.to_value, True, True, 5)
        l_hbox.pack_end(self.to_unit, True, True, 5)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.pack_start(u_hbox, False, False, 30)
        box.pack_start(l_hbox, False, False, 0)
        box.pack_start(self.ratio, True, False, 0)
        self.set_canvas(box)

        # Toolbar
        toolbarbox = ToolbarBox()

        activity_button = ActivityToolbarButton(self)

        toolbarbox.toolbar.insert(activity_button, 0)

        separator = Gtk.SeparatorToolItem()
        separator.set_expand(False)
        separator.set_draw(True)
        toolbarbox.toolbar.insert(separator, -1)

        # RadioToolButton
        self._length_btn = RadioToolButton()
        self._length_btn.connect('clicked',
                                 lambda w: self._update_combo(convert.length))
        # TRANS: https://en.wikipedia.org/wiki/Length
        self._length_btn.set_tooltip(_('Length'))
        self._length_btn.props.icon_name = 'length'

        self._volume_btn = RadioToolButton()
        self._volume_btn.connect('clicked',
                                 lambda w: self._update_combo(convert.volume))
        # TRANS: https://en.wikipedia.org/wiki/Volume
        self._volume_btn.set_tooltip(_('Volume'))
        self._volume_btn.props.icon_name = 'volume'
        self._volume_btn.props.group = self._length_btn

        self._area_btn = RadioToolButton()
        self._area_btn.connect('clicked',
                               lambda w: self._update_combo(convert.area))
        # TRANS: https://en.wikipedia.org/wiki/Area
        self._area_btn.set_tooltip(_('Area'))
        self._area_btn.props.icon_name = 'area'
        self._area_btn.props.group = self._length_btn

        self._weight_btn = RadioToolButton()
        self._weight_btn.connect('clicked',
                                 lambda w: self._update_combo(convert.weight))
        # TRANS: https://en.wikipedia.org/wiki/Weight
        self._weight_btn.set_tooltip(_('Weight'))
        self._weight_btn.props.icon_name = 'weight'
        self._weight_btn.props.group = self._length_btn

        self._speed_btn = RadioToolButton()
        self._speed_btn.connect('clicked',
                                lambda w: self._update_combo(convert.speed))
        # TRANS: https://en.wikipedia.org/wiki/Speed
        self._speed_btn.set_tooltip(_('Speed'))
        self._speed_btn.props.icon_name = 'speed'
        self._speed_btn.props.group = self._length_btn

        self._time_btn = RadioToolButton()
        self._time_btn.connect('clicked',
                               lambda w: self._update_combo(convert.time))
        # TRANS: https://en.wikipedia.org/wiki/Time
        self._time_btn.set_tooltip(_('Time'))
        self._time_btn.props.icon_name = 'time'
        self._time_btn.props.group = self._length_btn

        self._temp_btn = RadioToolButton()
        self._temp_btn.connect('clicked',
                               lambda w: self._update_combo(convert.temp))
        # TRANS: https://en.wikipedia.org/wiki/Temperature
        self._temp_btn.set_tooltip(_('Temperature'))
        self._temp_btn.props.icon_name = 'temp'
        self._temp_btn.props.group = self._length_btn

        #Circle
        self._circle_btn = RadioToolButton()
        self._circle_btn.connect('clicked',
                               lambda w: self._update_combo(convert.circle))
        self._circle_btn.set_tooltip(_('Angles of Circles'))
        self._circle_btn.props.icon_name = 'circle'
        self._circle_btn.props.group = self._length_btn

        #pressure
        self._pressure_btn = RadioToolButton()
        self._pressure_btn.connect('clicked',
                               lambda w: self._update_combo(convert.pressure))
        self._pressure_btn.set_tooltip(_('Pressure'))
        self._pressure_btn.props.icon_name = 'pressure'
        self._pressure_btn.props.group = self._length_btn

        #force
        self._force_btn = RadioToolButton()
        self._force_btn.connect('clicked',
                               lambda w: self._update_combo(convert.force))
        self._force_btn.set_tooltip(_('Force'))
        self._force_btn.props.icon_name = 'force'
        self._force_btn.props.group = self._length_btn

        #energy
        self._energy_btn = RadioToolButton()
        self._energy_btn.connect('clicked',
                               lambda w: self._update_combo(convert.energy))
        self._energy_btn.set_tooltip(_('Energy'))
        self._energy_btn.props.icon_name = 'energy'
        self._energy_btn.props.group = self._length_btn

        #Storage
        self._storage_btn = RadioToolButton()
        self._storage_btn.connect('clicked',
                               lambda w: self._update_combo(convert.storage))
        self._storage_btn.set_tooltip(_('Digital Storage'))
        self._storage_btn.props.icon_name = 'storage'
        self._storage_btn.props.group = self._length_btn

        toolbarbox.toolbar.insert(self._length_btn, -1)
        toolbarbox.toolbar.insert(self._volume_btn, -1)
        toolbarbox.toolbar.insert(self._area_btn, -1)
        toolbarbox.toolbar.insert(self._weight_btn, -1)
        toolbarbox.toolbar.insert(self._speed_btn, -1)
        toolbarbox.toolbar.insert(self._time_btn, -1)
        toolbarbox.toolbar.insert(self._temp_btn, -1)
        toolbarbox.toolbar.insert(self._circle_btn, -1)
        toolbarbox.toolbar.insert(self._pressure_btn, -1)
        toolbarbox.toolbar.insert(self._force_btn, -1)
        toolbarbox.toolbar.insert(self._energy_btn, -1)
        toolbarbox.toolbar.insert(self._storage_btn, -1)

        separator = Gtk.SeparatorToolItem()
        separator.set_expand(True)
        separator.set_draw(False)
        toolbarbox.toolbar.insert(separator, -1)

        stopbtn = StopButton(self)
        toolbarbox.toolbar.insert(stopbtn, -1)

        self.set_toolbar_box(toolbarbox)
        self._update_combo(convert.length)
        self.show_all()

    def _from_changed_cb(self, widget):
        direction = 'from'
        if isinstance(widget, Gtk.Entry):
            self._update_value(widget, direction)
        elif isinstance(widget, Gtk.ComboBox):
            if self.arrow.get_text() == '←':
                direction = 'to'
            self._update_unit(widget, direction)

    def _to_changed_cb(self, widget):
        direction = 'to'
        if isinstance(widget, Gtk.Entry):
            self._update_value(widget, direction)
        elif isinstance(widget, Gtk.ComboBox):
            if self.arrow.get_text() == '→':
                direction = 'from'
            self._update_unit(widget, direction)

    def _update_value(self, entry, direction):
        try:
            num_value = str(entry.get_text())
            num_value = float(num_value.replace(',', ''))
            decimals = str(len(str(num_value).split('.')[-1]))
            fmt = '%.' + decimals + 'f'
            new_value = locale.format(fmt, float(num_value))
            new_value = new_value.rstrip("0")
            if new_value[-1] == '.':
                new_value = new_value[0:len(new_value) - 1]
            convert_value = str(self.convert(num_value, direction))
            decimals = str(len(convert_value.split('.')[-1]))
            fmt = '%.' + decimals + 'f'
            new_convert = locale.format(fmt, float(convert_value))
            new_convert = new_convert.rstrip("0")
            if new_convert[-1] == '.':
                new_convert = new_convert[0:len(new_convert) - 1]
            self.change_result(new_value, new_convert, direction)
        except ValueError:
            self.change_result('', '', direction)

    def _update_unit(self, combo, direction):
        if direction == 'from':
            self._update_value(self.from_value, direction)
        elif direction == 'to':
            self._update_value(self.to_value, direction)

    def change_result(self, new_value, new_convert, direction):
        if direction == 'from':
            self.to_value.handler_block_by_func(self._to_changed_cb)
            self.to_value.handler_block_by_func(self._insert_text_cb)
            self.to_value.set_text(new_convert)
            self.to_value.handler_unblock_by_func(self._insert_text_cb)
            self.to_value.handler_unblock_by_func(self._to_changed_cb)

            self.arrow.set_text("→")
            self.label1.set_markup('<big>From value</big>')
            self.label2.set_markup('<big>From unit</big>')
            self.label3.set_markup('<big>To value</big>')
            self.label4.set_markup('<big>To unit</big>')
            if new_convert != '' and new_value != '':
                text = '%s %s ~ %s %s' % (
                    new_value, self._get_active_text(self.from_unit),
                    new_convert, self._get_active_text(self.to_unit))
                self.ratio.set_text(text)
            else:
                self.ratio.set_text('')

        elif direction == 'to':
            self.from_value.handler_block_by_func(self._from_changed_cb)
            self.from_value.handler_block_by_func(self._insert_text_cb)
            self.from_value.set_text(new_convert)
            self.from_value.handler_unblock_by_func(self._insert_text_cb)
            self.from_value.handler_unblock_by_func(self._from_changed_cb)

            self.arrow.set_text("←")
            self.label1.set_markup('<big>To value</big>')
            self.label2.set_markup('<big>To unit</big>')
            self.label3.set_markup('<big>From value</big>')
            self.label4.set_markup('<big>From unit</big>')
            if new_convert != '' and new_value != '':
                text = '%s %s ~ %s %s' % (
                    new_convert, self._get_active_text(self.from_unit),
                    new_value, self._get_active_text(self.to_unit))
                self.ratio.set_text(text)
            else:
                self.ratio.set_text('')

    def _update_combo(self, data):
        self._liststore.clear()
        self.dic = data
        keys = self.dic.keys()
        keys.sort()
        for x in keys:
            self._liststore.append(['%s' % (x)])
        if keys[0] == 'Cables':
            self.from_unit.set_active(12)
            self.to_unit.set_active(12)
        elif keys[0] == 'Cubic Centimeter':
            self.from_unit.set_active(3)
            self.to_unit.set_active(3)
        elif keys[0] == 'Acre':
            self.from_unit.set_active(4)
            self.to_unit.set_active(4)
        elif keys[0] == 'Carat':
            self.from_unit.set_active(2)
            self.to_unit.set_active(2)
        elif keys[0] == 'Centimeters/Minute':
            self.from_unit.set_active(9)
            self.to_unit.set_active(9)
        elif keys[0] == 'Day':
            self.from_unit.set_active(8)
            self.to_unit.set_active(8)
        elif keys[0] == 'Celsius':
            self.from_unit.set_active(2)
            self.to_unit.set_active(2)
        elif keys[0] == 'Degrees':
            self.from_unit.set_active(1)
            self.to_unit.set_active(1)
        elif keys[0] == 'Atmosphere (atm)':
            self.from_unit.set_active(2)
            self.to_unit.set_active(2)
        elif keys[0] == 'Dyne (dyn)':
            self.from_unit.set_active(2)
            self.to_unit.set_active(2)
        elif keys[0] == 'Calories (cal)':
            self.from_unit.set_active(2)
            self.to_unit.set_active(2)
        elif keys[0] == 'Bit':
            self.from_unit.set_active(1)
            self.to_unit.set_active(1)
        else:
            pass
        self.show_all()

    def _get_active_text(self, combobox):
        active = combobox.get_active()
        keys = self.dic.keys()
        keys.sort()
        if active < 0:
            active = 0
        text = keys[active]
        if '<sup>' in text:
            text = text.split('<b>')[1].split('</b>')[0]
        return text

    def convert(self, num_value, direction):
        if direction == 'from':
            unit = self._get_active_text(self.from_unit)
            to_unit = self._get_active_text(self.to_unit)
        elif direction == 'to':
            unit = self._get_active_text(self.to_unit)
            to_unit = self._get_active_text(self.from_unit)
        return convert.convert(num_value, unit, to_unit, self.dic)

    def _insert_text_cb(self, entry, text, length, position):
        for char in text:
            if char == "-" and \
               entry.get_text() is "" and len(text) == 1:
                return False
            elif not re.match('[0-9,.]', char):
                entry.emit_stop_by_name('insert-text')
                return True
        return False
