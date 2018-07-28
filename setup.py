import io
import os
import sys
from setuptools import setup


NAME = 'MetaClean'
DESCRIPTION='Python tool to clean privacy depending metadata from files'
VERSION = 0.1
URL='http://github.com/...'
REQUIRES_PYTHON='>=3.6.0'
AUTHOR='N-Three'
EMAIL='n3@asd.com'


# What packages are required for this module to be executed?
REQUIRED = [
    'Click', 'json'
]


here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


setup(

name=NAME,
version=VERSION,
description=DESCRIPTION,
long_description=DESCRIPTION,
long_description_content_type='text/markdown',
author=AUTHOR,
author_email=EMAIL,
python_requires=REQUIRES_PYTHON,
url=URL,

py_modules=['core'],
    install_requires=[
        'Click',
    ],

    entry_points={
        'console_scripts': ['metaclean=main:cli'],
    },

)
