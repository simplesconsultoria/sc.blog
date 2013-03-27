# -*- coding: utf-8 -*-

from Acquisition import aq_inner
from collective.nitf.content import INITF
from five import grok
from plone.app.layout.viewlets.interfaces import IAboveContent
from plone.directives import dexterity
from sc.blog.content import IBlog
from sc.blog.interfaces import IBlogLayer
from zope.interface import Interface

grok.templatedir('templates')


class View(dexterity.DisplayForm):
    """Default view. Looks like a standard Folder Full View.
    """
    grok.context(IBlog)
    grok.layer(IBlogLayer)
    grok.template('folder_full_view')
    grok.require('zope2.View')


class BlogSummaryView(dexterity.DisplayForm):
    """Looks like a standard Folder Summary View.
    """
    grok.context(IBlog)
    grok.layer(IBlogLayer)
    grok.name('blog_summary_view')
    grok.template('folder_summary_view')
    grok.require('zope2.View')


class BlogHeader(grok.Viewlet):
    """A viewlet to include a header in the container (Blog) and contained
    (News Article) elements.
    """
    grok.name('sc.blog.blogheader')
    grok.context(Interface)
    grok.layer(IBlogLayer)
    grok.require('zope2.View')
    grok.viewletmanager(IAboveContent)

    def update(self):
        self.context = aq_inner(self.context)
        # is context a Blog?
        self.is_blog = IBlog.providedBy(self.context)
        # is context a News Article inside a Blog?
        self.is_post = INITF.providedBy(self.context) and \
            IBlog.providedBy(self.context.__parent__)

    def available(self):
        return self.is_blog or self.is_post

    def blog(self):
        if self.is_blog:
            return self.context
        if self.is_post:
            return self.context.__parent__

    def blog_url(self):
        return self.blog().absolute_url()
