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

    # def __before_publishing_traverse__(self, arg1, arg2=None):
    #     """ Pre-traversal hook.
    #     """
    #     # XXX hack around a bug(?) in BeforeTraverse.MultiHook
    #     REQUEST = arg2 or arg1

    #     # XXX reorder interfaces
    #     noLongerProvides(REQUEST, INITFLayer)
    #     alsoProvides(REQUEST, IBlogSkin)
    #     alsoProvides(REQUEST, INITFLayer)

    #     super(Container,
    #           self).__before_publishing_traverse__(arg1, arg2)
