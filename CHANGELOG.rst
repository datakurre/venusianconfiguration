Changelog
=========

1.1.1 (unreleased)
------------------

- Nothing changed yet.


1.1.0 (2018-01-17)
------------------

- Drop z3c.autoinclude plugin entrypoint for plone to fix issues with where
  z3c.autoinclude included wrong packages on and pip-installed Plone. This
  will disable the experimental ZCML directives from meta.zcml to be loaded
  by default with Plone.
  [datakurre]

1.0.2 (2017-12-21)
------------------

- Fix issue where default configuration directive being mutable caused
  unexpected behavior
  [datakurre]

1.0.1 (2016-09-21)
------------------

- Fix issue where zope.deferredimported module was not recognized as module
  [datakurre]

1.0.0 (2016-04-19)
------------------

- First release.
