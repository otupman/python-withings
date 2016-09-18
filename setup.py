#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='withings',
    version='0.4.0',
    description="Library for the Withings API",
    author='Maxime Bouroumeau-Fuseau',
    author_email='maxime.bouroumeau@gmail.com',
    url="https://github.com/maximebf/python-withings",
    license="MIT License",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'click',
        'requests',
        'requests-oauth',
        'requests-oauthlib',
    ],
    entry_points={
        'console_scripts': [
            'withings = withings.__main__:main',
        ]
    },
)
