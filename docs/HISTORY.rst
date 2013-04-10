Changelog
---------

Because you have to know where your towel is.

1.0a3 (2013-04-10)
^^^^^^^^^^^^^^^^^^

- Refactor template of blog header: now it will display the blog image, if
  present, or the blog title, if not. [hvelarde]

- Image field is no longer required by default. [hvelarde]

- In order to fix ordering in plone.abovecontent viewlet manager, we had to
  register the plone.path_bar viewlet before everything and then register the
  sc.blog.blogheader viewlet after everything. [hvelarde]


1.0a2 (2013-04-04)
^^^^^^^^^^^^^^^^^^

- Fix batch size and ordering of posts on blogs. Now up to 10 posts are shown
  per page and they are sorted by effective date in descending order.
  [hvelarde]

- Disallow comments on blogs by default as users comment on posts. [hvelarde]


1.0a1 (2013-03-15)
^^^^^^^^^^^^^^^^^^

- Initial release.
