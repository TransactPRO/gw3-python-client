#!/usr/bin/env python

import setuptools

MAINTAINER_NAME = 'Transact Pro'
MAINTAINER_EMAIL = 'support@transactpro.lv'
URL_GIT = 'https://github.com/TransactPRO/gw3-python-client'

try:
    import pypandoc

    LONG_DESCRIPTION = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError, OSError, RuntimeError):
    LONG_DESCRIPTION = ''

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

required = [
    'requests',
]

setuptools.setup(
    name='transactpro-gw3-client',
    version='1.7.1',
    description='Transact PRO Gateway3 implementation in Python.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author='Transact Pro',
    author_email='support@transactpro.net',
    install_requires=required,
    url=URL_GIT,
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=CLASSIFIERS,
    keywords='GW3 gateway3 integration gateway TransactPRO python python3',
    python_requires='>=3.6',
)
