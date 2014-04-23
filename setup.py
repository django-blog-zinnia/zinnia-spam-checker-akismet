"""Setup script of zinnia-spam-checker-akismet"""
from setuptools import setup
from setuptools import find_packages

import zinnia_akismet

setup(
    name='zinnia-spam-checker-akismet',
    version=zinnia_akismet.__version__,

    description=('Anti-spam protections for django-blog-zinnia '
                 'with Akismet or Typepad'),
    long_description=open('README.rst').read(),
    keywords='django, zinnia, spam, akismet, typepad',

    author=zinnia_akismet.__author__,
    author_email=zinnia_akismet.__email__,
    url=zinnia_akismet.__url__,

    packages=find_packages(),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=zinnia_akismet.__license__,
    include_package_data=True,
    zip_safe=False,
    install_requires=['akismet>=0.2.0']
)
