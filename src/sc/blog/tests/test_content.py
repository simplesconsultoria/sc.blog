# -*- coding: utf-8 -*-

from sc.blog.content import IBlog
from sc.blog.browser import post
from sc.blog.testing import INTEGRATION_TESTING
from plone.app.referenceablebehavior.referenceable import IReferenceable
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from plone.uuid.interfaces import IAttributeUUID
from zope.component import createObject
from zope.component import queryUtility
from zope.interface import alsoProvides
from collective.nitf.interfaces import INITFLayer

import unittest
from sc.blog.interfaces import IBlogSkin


class ContentTypeTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

        self.folder.invokeFactory('Blog', 'b1')
        self.b1 = self.folder['b1']

    def test_adding(self):
        self.assertTrue(IBlog.providedBy(self.b1))

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Blog')
        self.assertIsNotNone(fti)

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Blog')
        schema = fti.lookupSchema()
        self.assertEqual(IBlog, schema)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Blog')
        factory = fti.factory
        new_object = createObject(factory)
        self.assertTrue(IBlog.providedBy(new_object))

    def test_is_referenceable(self):
        self.assertTrue(IReferenceable.providedBy(self.b1))
        self.assertTrue(IAttributeUUID.providedBy(self.b1))

    def test_post_view(self):
        self.b1.invokeFactory('collective.nitf.content', 'n1')
        # provide the nitf layer...
        alsoProvides(self.layer['request'], INITFLayer)
        view = self.b1.n1.unrestrictedTraverse("view")
        # nitf standard view
        self.assertFalse(isinstance(view, post.View))
        # XXX: simulate a traverse
        self.layer['request']['TraversalRequestNameStack'] = []
        self.b1.__before_publishing_traverse__(self.layer['request'])        
        view = self.b1.n1.unrestrictedTraverse("view")
        # nitf post view
        self.assertTrue(isinstance(view, post.View))
