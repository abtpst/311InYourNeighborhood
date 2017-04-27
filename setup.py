from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='311InYourNeighborhood',
    version='1.0.0',
    description='311InYourNeighborhood',
    long_description=long_description,
    url='https://github.com/awgreene/311InYourNeighborhood'
)
