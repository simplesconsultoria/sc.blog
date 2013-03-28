# -*- coding: utf-8 -*-

from collective.nitf.browser import View as NITFView
from five import grok
from sc.blog.interfaces import IBlogLayer

grok.templatedir('templates')


class View(NITFView):
    """A post is, in fact, a News Article with a simplified view.
    """
    grok.layer(IBlogLayer)
    grok.name('post')
    grok.template('nitf_custom_view')
