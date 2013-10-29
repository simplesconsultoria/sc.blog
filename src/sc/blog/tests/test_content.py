# -*- coding: utf-8 -*-

from plone.app.referenceablebehavior.referenceable import IReferenceable
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from plone.uuid.interfaces import IAttributeUUID
from sc.blog.content import IBlog
from sc.blog.testing import INTEGRATION_TESTING
from zope.component import createObject
from zope.component import queryUtility
from zope.interface import alsoProvides
from plone.app.content.browser.folderfactories import _allowedTypes

import unittest


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

    def test_subblog(self):
        request = self.layer['request']
        # Blogs can't contain Blogs
        self.assertTrue('Blog' in [i.id for i in _allowedTypes(request, self.folder)])
        self.assertFalse('Blog' in [i.id for i in _allowedTypes(request, self.b1)])
        self.b1.invokeFactory('Folder', 'subfolder')
        self.assertFalse('Blog' in [i.id for i in _allowedTypes(request, self.b1.subfolder)])
