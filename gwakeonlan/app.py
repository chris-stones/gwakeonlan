##
#     Project: gWakeOnLAN
# Description: Wake up your machines using Wake on LAN
#      Author: Fabio Castelli (Muflone) <webreg@vbsimple.net>
#   Copyright: 2009-2013 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

import os.path
from gi.repository import Gtk
from gi.repository import Gio
from gwakeonlan.ui import MainWindow
from gwakeonlan.constants import *

class Application(Gtk.Application):
  def __init__(self):
    super(self.__class__, self).__init__(application_id=APP_ID)
    self.connect("activate", self.activate)
    self.connect('startup', self.startup)

  def startup(self, application):
    "Configure the application during the startup"
    self.ui = MainWindow(self)
    # Add the actions related to the app menu
    action = Gio.SimpleAction(name="about")
    action.connect("activate", self.on_app_about_activate)
    self.add_action(action)

    action = Gio.SimpleAction(name="quit")
    action.connect("activate", self.on_app_quit_activate)
    self.add_action(action)
    # Add the app menu
    builder = Gtk.Builder()
    builder.add_from_file(os.path.join(DIR_UI, 'appmenu.ui'))
    menubar = builder.get_object('app-menu')
    self.set_app_menu(menubar)

  def activate(self, application):
    "Execute the application"
    self.ui.run()

  def on_app_about_activate(self, action, data):
    "Show the about dialog from the app menu"
    self.ui.on_btnAbout_clicked(self)

  def on_app_quit_activate(self, action, data):
    "Quit the application from the app menu"
    self.ui.on_winMain_delete_event(self, None)
