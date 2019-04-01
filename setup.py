#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'molssi_workflow>=0.1',
    'molssi_util>=0.1'
    # TODO: put any other package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(emarinri): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='cassandra_step',
    version='0.1.0',
    description="Cassandra is a Monte Carlo molecular simulation package.",
    long_description=readme + '\n\n' + history,
    author="Eliseo Marin-Rimoldi",
    author_email='meliseo@vt.edu',
    url='https://github.com/emarinri/cassandra_step',
    packages=find_packages(include=['cassandra_step']),
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='cassandra_step',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Materials Science',
        'Topic :: Scientific/Engineering :: Computational Materials Science',
        'Topic :: Scientific/Engineering :: Computational Molecular Science',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3  :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    entry_points={
        'org.molssi.workflow': [
            'Cassandra = cassandra_step:CassandraStep',
        ],
        'org.molssi.workflow.tk': [
            'Cassandra = cassandra_step:CassandraStep',
        ],
    }
)