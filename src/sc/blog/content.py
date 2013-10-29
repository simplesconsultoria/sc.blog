# -*- coding: utf-8 -*-

# from collective.nitf.interfaces import INITFLayer
from five import grok
from plone.dexterity.content import Container
from plone.directives import form
from plone.namedfile.field import NamedBlobImage
from sc.blog import _
from sc.blog.interfaces import IBlogSkin
from zope import schema
from zope.interface import alsoProvides
from zope.interface import noLongerProvides


class IBlog(form.Schema):
    """A Blog.
    """

    author = schema.TextLine(
        title=_(u'Author'),
        default=u'',
    )

    image = NamedBlobImage(
        title=_(u"Image"),
        required=False,
    )


class Blog(Container):
    """A Blog is a container of News Articles.
    """
    grok.implements(IBlog)


def blog_added(ob, event):
    # inside blogs you can't add blogs
    ob.manage_permission("sc.blog: Add Blog")

