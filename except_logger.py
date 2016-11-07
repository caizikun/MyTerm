#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
#############################################################################
##
## Copyright (c) 2016, gamesun
## All right reserved.
##
## This file is part of BdpTerm.
##
## BdpTerm is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## BdpTerm is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with BdpTerm.  If not, see <http://www.gnu.org/licenses/>.
##
#############################################################################


import io, logging, traceback

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
    filename="error.log",
    filemode='a'
)

logger = logging.getLogger('ERR')

def exceptHook(excType, excValue, tracebackobj):
    """
    Global function to catch unhandled exceptions.

    @param excType exception type
    @param excValue exception value
    @param tracebackobj traceback object
    """

    separator = '-' * 80 + '\n'
    tbinfofile = io.StringIO()
    traceback.print_tb(tracebackobj, None, tbinfofile)
    tbinfofile.seek(0)
    tbinfo = tbinfofile.read()
    errmsg = '%s: \n%s' % (str(excType), str(excValue))
    msg = separator + errmsg + '\n\n' + tbinfo + separator

    for line in msg.rstrip().splitlines():
        logger.log(logging.ERROR, line.rstrip())