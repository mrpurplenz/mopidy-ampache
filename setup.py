from __future__ import unicode_literals

import re
from setuptools import setup, find_packages


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']

setup(
    name='Mopidy-Ampache',
    version=get_version('mopidy_ampache/__init__.py'),
    url='http://github.com/mrpurplenz/mopidy-ampache/',
    license='MIT',
    author='mrpurple',
    author_email='mrpurplenz@gmail.com',
    description='Ampache extension for Mopidy',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 1.0',
        'Pykka >= 1.1',
        'py-mpache',
    ],
    entry_points={
        b'mopidy.ext': [
            'ampache = mopidy_ampache:AmpacheExtension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
