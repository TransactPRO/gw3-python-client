#!/usr/bin/env python

from setuptools import setup

MAINTAINER_NAME = 'Artjoms Nemiro'
MAINTAINER_EMAIL = 'artjom.nemiro@gateway.lv'
URL_GIT = 'https://github.com/TransactPRO/GW3-python-integration'

try:
    import pypandoc

    LONG_DESCRIPTION = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError, OSError, RuntimeError):
    LONG_DESCRIPTION = ''

CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

required = [
    'requests'
]

packages = ['gateway', 'gateway/builders', 'gateway/operations', 'gateway/data_sets']

setup(
    name='transact-pro/gw3',
    version='1.0.0',
    description='Transact PRO Gateway3 implementation in Python.',
    long_description=LONG_DESCRIPTION,
    author='Transact pro',
    author_email='support@transactpro.lv',
    maintainer=MAINTAINER_NAME,
    maintainer_email=MAINTAINER_EMAIL,
    install_requires=required,
    # url=URL_GIT,
    # download_url='',
    packages=packages,
    platforms=['Platform Independent'],
    license='MIT',
    classifiers=CLASSIFIERS,
    keywords='GW3, gateway3, gw3 integration, gateway, Transact PRO, python, python3',
)
