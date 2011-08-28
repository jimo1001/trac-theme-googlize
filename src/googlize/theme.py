# -*- coding: utf-8 -*-
#
# provide a Trac Theme.
# The plugin uses ThemeEnginePlugin.
#
# Created on  2011/07/17
# @author: jimo1001

from trac.core import *
from themeengine.api import ThemeBase


class GooglizeTheme(ThemeBase):
    """Trac Theme like Google"""
    template = htdocs = css = screenshot = True
