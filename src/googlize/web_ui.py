# -*- coding: utf-8 -*-
#
# Web UI
#
# Created on  2011/07/17
# @author: jimo1001

from trac.core import *
from trac.web.api import ITemplateStreamFilter

from genshi.filters.transform import StreamBuffer, Transformer
from genshi.builder import tag

class GooglizeModule(Component):

    implements(ITemplateStreamFilter)

    # ITemplateStreamFilter a method

    def filter_stream(self, req, _method, filename, stream, data):
        buf = None
        if filename == 'wiki_view.html':
            pagename = data.get('pagename') or 'Wiki'
        else:
            buf = StreamBuffer()
            pagename = data.get('pagename') or req.path_info.lstrip('/').split('/')[0]
            stream = stream | Transformer('.//div[@id="content"]/h1').cut(buf).buffer()
        stream = stream | Transformer('.//div[@id="ab-name"]').append(buf or tag.h1(pagename))
        return stream
