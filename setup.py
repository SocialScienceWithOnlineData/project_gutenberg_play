#!/usr/bin/env python
### cribbed from https://github.com/maet3608/minimal-setup-py/blob/master/setup.py
from setuptools import setup, find_packages

setup(
    name='project_gutenberg_play',
    version='0.1.0',
    url='https://github.com/SocialScienceWithOnlineData/project_gutenberg_play.git',
    author='Seth Frey',
    author_email='sfrey@ucdavis.edu',
    description='Helper functions for exploring project gutenberg texts via URL',
    packages=find_packages(),
    license='MIT',
)
