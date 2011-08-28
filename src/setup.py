#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# provide a theme for Trac.
#
# (C) 2011 jimo1001
# All rights reserved.
#
# Created on  2011/08/28
# @author: jimo1001

from setuptools import setup

setup(
    name = 'TracThemeGooglize',
    version = '0.0.1',
    packages = ['googlize'],
    package_data = {
        'googlize': [
            'templates/*.html',
            'htdocs/*.png',
            'htdocs/*.css',
            'htdocs/img/*.gif',
            'htdocs/img/*.jpg',
	    'htdocs/img/*.png'
        ]
    },
    author = 'jimo1001',
    author_email = 'jimo1001@gmail.com',
    description = 'like Google Theme',
    license = 'BSD',
    keywords = 'trac plugin theme',
    url = '',
    classifiers = [
        'Framework :: Trac',
    ],
    install_requires = ['Trac', 'TracThemeEngine>=2.0'],

    entry_points = {
        'trac.plugins': [
            'googlize.theme = googlize.theme',
        ]
    },
)
