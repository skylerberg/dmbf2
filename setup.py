from setuptools import setup, find_packages
from os.path import join, dirname

import dmbf2


setup(
    name='dmbf2',
    version=dmbf2.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    )