# -*- coding: utf-8 -*-
#
# Web UI
#
# Created on  2011/07/17
# @author: jimo1001

from trac.web.api import IRequestFilter
from trac.core import *

class GooglizeModule(Component):

    implements(IRequestFilter)

    # IRequestFilter methods

    def pre_process_request(self, req, handler):
        return handler

    def post_process_request(self, req, template, data, content_type):
        data['ab_name'] = 'Wiki'
        return template, data, content_type
