#! /usr/bin/env python3
# Copyright (C) 2020 Sebastian Pipping <sebastian@pipping.org>
# Licensed under GPL v3 or later

from setuptools import find_packages, setup

from git_delete_merged_branches._metadata import APP, VERSION

setup(
    name=APP,
    version=VERSION,

    license='GPLv3+',
    description='Command-line tool to delete merged Git branches',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',

    author='Sebastian Pipping',
    author_email='sebastian@pipping.org',
    url=f'https://github.com/hartwork/{APP}',

    python_requires='>=3.6',
    setup_requires=[
        'setuptools>=38.6.0',  # for long_description_content_type
    ],
    install_requires=[
        'pick>=0.6.7',
    ],
    tests_require=[
        'parameterized',
    ],

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            f'{APP} = git_delete_merged_branches.__main__:main',
        ],
    },

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Version Control',
        'Topic :: Software Development :: Version Control :: Git',
    ],
)
