#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#
#  Copyright 2021
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#TEEST TEST TEST
import salt.config
import salt.loader
import salt.client
import sys

opts = salt.config.master_config('/etc/salt/master')
local = salt.client.LocalClient()

#Returns a dictionary list of all minions and if they respond to ping or not.
pinglist = local.cmd('*', 'test.ping')

#Checking if all minions responded or not.  Exits script if not all respond.
res = True
for i in pinglist:
	if not pinglist[i]:
		res = False
		break

if res == False:
	print('Not All Minions Responded... Aborting Script')
	sys.exit(1)
else:
	print('All Minions Responded... Proceeding')
