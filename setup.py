#!/usr/bin/env python

from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='bak',
      version='0.4.3',
      license='GPLv2',
      description='Backup a file or directory, defaults to same path with suffix .bak',
      author='Jonathan Mainguy',
      author_email='jon@soh.re',
      url='https://github.com/Jmainguy/bak',
      scripts=['bak', 'unbak'],
      install_requires=[
          'xattr',
      ],
      long_description=long_description,
      long_description_content_type='text/markdown'
     )
