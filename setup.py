#!/usr/bin/env python

from setuptools import setup

setup(name='bak',
      version='0.4.2',
      license='GPLv2',
      description='Backup a file, defaults to same path and .bak',
      author='Jonathan Mainguy',
      author_email='jon@soh.re',
      url='https://github.com/Jmainguy/bak',
      scripts=['bak', 'unbak'],
      install_requires=[
          'xattr',
      ],
     )
