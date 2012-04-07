# -*- coding: utf-8 -*-
#
# Created on  2011/07/17
# @author: jimo1001

from trac.core import *

class ISubmenuItemProvider(Interface):

    @staticmethod
    def match_request(req, template):
        """Return whether the handler wants to process the given request and template."""

    @staticmethod
    def get_submenu_items(req, data):
        """Return a list of side menu items."""
