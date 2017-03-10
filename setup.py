#!/usr/bin/env python

from distutils.core import setup
import sys
import warnings

if sys.version < '3':
    warnings.warn(
        'Python 2 is not officially supported by Transact PRO  with Gateway3. '
        'If you have any questions, please file an issue on Github',
        DeprecationWarning)
    raise RuntimeError('Please install higher version of Python.')

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

MAINTAINER_NAME = 'Artjoms Nemiro'
MAINTAINER_EMAIL = 'artjom.nemiro@gateway.lv'
URL_GIT = 'https://github.com/TransactPRO/gw3-python-client'

try:
    import pypandoc

    LONG_DESCRIPTION = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError, OSError, RuntimeError):
    LONG_DESCRIPTION = ''

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
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
    'requests',
    'ssl'
]

packages = [
    'gateway',
    'gateway/builders',
    'gateway/operations',
    'gateway/data_sets',
    'gateway/utils',
    'gateway/http'
]

tests_packages = [
    'unittest',
    'mock'
]

setup(
    name='transact-pro/gw3-client',
    cmdclass={'build_py': build_py},
    version='1.0.0',
    description='Transact PRO Gateway3 implementation in Python.',
    long_description=LONG_DESCRIPTION,
    author='Transact pro',
    author_email='support@transactpro.lv',
    maintainer=MAINTAINER_NAME,
    maintainer_email=MAINTAINER_EMAIL,
    install_requires=required,
    url=URL_GIT,
    download_url='',
    packages=packages,
    tests_require=tests_packages,
    platforms=['Platform Independent'],
    license='MIT',
    classifiers=CLASSIFIERS,
    keywords='GW3, gateway3, gw3 integration, gateway, Transact PRO, python, python3',
)
