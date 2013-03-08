# -*- coding: utf-8 -*-

from five import grok
from plone.dexterity.content import Container
from plone.directives import form
from plone.namedfile.field import NamedBlobImage
from sc.blog import _
from zope import schema

grok.templatedir('templates')


class IBlog(form.Schema):
    """A Blog.
    """

    author = schema.TextLine(
        title=_(u'Author'),
        default=u'',
    )

    image = NamedBlobImage(
        title=_(u"Image")
    )


class Blog(Container):
    """A Blog is a container of News Articles.
    """
    grok.implements(IBlog)
