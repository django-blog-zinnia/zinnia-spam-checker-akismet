===========================
Zinnia-spam-checker-akismet
===========================

Zinnia-spam-checker-akismet is a package providing spam protection on
comments for `django-blog-zinnia`_ via `Akismet`_ or `Typepad AntiSpam`_.

Installation
============

Simply install the package on your system: ::

  $ pip install zinnia-spam-checker-akismet

The `python-akismet`_ will also be installed as a dependency.

Using Akismet
-------------

Put this setting to enable the Akismet spam checker backend:

  ``ZINNIA_SPAM_CHECKER_BACKENDS = ('zinnia_akismet.akismet',)``

Then define your API key in the settings:

  ``AKISMET_SECRET_API_KEY = 'Your key'``

Get your free API key at http://akismet.com/signup/ if you don't have one.

Using Typepad AntiSpam
----------------------

Put this setting to enable the Typepad spam checker backend:

  ``ZINNIA_SPAM_CHECKER_BACKENDS = ('zinnia_akismet.typepad',)``

Then define your API key in the settings:

  ``TYPEPAD_SECRET_API_KEY = 'Your key'``

Why Typepad is included in this package ?

For conveniency because the Typepad AntiSpam use the same API as
Akismet, they share the same dependancy to the `python-akismet`_
module.

Note that you can combine the two spam checkers like this: ::

  ZINNIA_SPAM_CHECKER_BACKENDS = (
      'zinnia_akismet.akismet',
      'zinnia_akismet.typepad')


.. _django-blog-zinnia: http://django-blog-zinnia.com
.. _Akismet: http://akismet.com/
.. _Typepad AntiSpam: http://antispam.typepad.com/
.. _python-akismet: https://pypi.python.org/pypi/akismet
