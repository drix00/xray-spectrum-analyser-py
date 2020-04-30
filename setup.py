#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: setup
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Setup script for the project.
"""

###############################################################################
# Copyright 2020 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# Standard library modules.
import os.path
import io
import sys

# Third party modules.
from setuptools import setup, find_namespace_packages
# noinspection PyPep8Naming
from setuptools.command.test import test as TestCommand

# Local modules.

# Project modules.
from xrayspectrumanalyser import __author__, __email__, __version__, __project_name__

# Globals and constants variables.
here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


long_description = read('README.rst')

requirements = read("requirements.txt")


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(
    name=__project_name__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    maintainer=__author__,
    maintainer_email=__email__,
    description="",
    long_description=long_description,
    keywords="python science physics",
    url="https://github.com/drix00/xray-spectrum-analyser-py",
    project_urls={
        "Bug Tracker": "https://github.com/drix00/xray-spectrum-analyser-py/issues",
        "Documentation": "https://xray-spectrum-analyser-py.readthedocs.io/",
        "Source Code": "https://github.com/drix00/xray-spectrum-analyser-py",
    },

    packages=find_namespace_packages(),
    platforms='any',
    zip_safe=False,
    cmdclass={'test': PyTest},

    install_requires=requirements,
    tests_require=['pytest', 'coverage', 'pytest-cov'],
    extras_require={
        'testing': ['pytest', 'coverage', 'pytest-cov'],
        'develop': ['setuptools', 'Sphinx', 'sphinx-rtd-theme', 'pytest', 'coverage', 'pytest-cov']
    },

    license="Apache Software License 2.0",
    license_file="LICENSE",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics'
    ],
)
