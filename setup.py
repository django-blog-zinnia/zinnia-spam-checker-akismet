"""Setup script of zinnia-spam-checker-akismet"""
from setuptools import setup
from setuptools import find_packages

setup(
    name='zinnia-spam-checker-akismet',
    version='1.0',

    description=('Anti-spam protections for django-blog-zinnia '
                 'with Akismet or Mollom'),
    long_description=open('README.rst').read(),
    keywords='django, zinnia, spam, akismet, mollom',

    author='Fantomas42',
    author_email='fantomas42@gmail.com',
    url='https://github.com/Fantomas42/zinnia-spam-checker-akismet',

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

    license='BSD License',
    include_package_data=True,
    zip_safe=False,
    install_requires=['akismet']
)
