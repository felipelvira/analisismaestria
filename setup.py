# Setup file for machine learning project
# run after download project from bitbucket

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command



	# # Global variables # #

# Package meta-data.
NAME = 'core'
DESCRIPTION = 'Proyecto Análisis de Datos (Maestría en contabilidad)'
URL = ''
EMAIL = 'felipe.elvira.garcia@outlook.com'
AUTHOR = 'Felipe Elvira'

# What packages are required for this module to be executed?
REQUIRED = [ 'core' ]


here = os.path.abspath(os.path.dirname(__file__))

# Load the package's __version__.py module as a dictionary.
about = {}
with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec(f.read(), about)



# Where the magic happens:
setup(
    name=NAME,
    version=0.0.1, #about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
)