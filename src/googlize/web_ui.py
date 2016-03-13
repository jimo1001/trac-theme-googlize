# -*- coding: utf-8 -*-
#
# Created on  2011/07/17
# @author: jimo1001

from trac.core import *
from trac.config import Option
from trac.web.api import IRequestFilter, ITemplateStreamFilter

from genshi.filters.transform import StreamBuffer, Transformer
from genshi.builder import tag

from googlize.api import ISubmenuItemProvider

class GooglizeModule(Component):

    implements(IRequestFilter, ITemplateStreamFilter)
    submenu_item_providers = ExtensionPoint(ISubmenuItemProvider)

    theme = Option('theme', 'theme')

    # IRequestFilter methods

    def pre_process_request(self, _req, handler):
        return handler

    def post_process_request(self, req, template, data, content_type):
        if self.theme == 'googlize':
            for provider in self.submenu_item_providers:
                if provider.match_request(req, template):
                    provider.get_submenu_items(req, data)
        return template, data, content_type

    # ITemplateStreamFilter a method

    def filter_stream(self, req, _method, filename, stream, data):
        if self.theme == 'googlize':
            buf = None
            if filename == 'wiki_view.html':
                pagename = data.get('pagename') or 'Wiki'
            else:
                buf = StreamBuffer()
                pagename = data.get('pagename') or req.path_info.lstrip('/').split('/')[0]
                stream = stream | Transformer('.//div[@id="content"]/h1').cut(buf).buffer()
            stream = stream | Transformer('.//div[@id="ab-name"]').append(buf or tag.h1(pagename))

            for provider in self.submenu_item_providers:
                if provider.match_request(req, filename):
                    pass
        return stream
