#!/usr/bin/env python

# Copyright (C) 2019 SignalFx, Inc. All rights reserved.
from os import path

from setuptools import setup

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]

for pkg in ('signalfx_gcf', 'signalfx_lambda'):
    vars = {}

    with open(path.join(pkg, 'version.py')) as f:
        exec(f.read(), vars)

    with open(path.join(pkg, 'README.rst')) as readme:
        long_description = readme.read()

    setup(
        name=vars['name'],  # noqa
        version=vars['version'],  # noqa
        author='SignalFx, Inc',
        author_email='info@signalfx.com',
        description='SignalFx Python Serverless Wrapper',
        license='Apache Software License v2',
        long_description=long_description,
        long_description_content_type='text/x-rst',
        zip_safe=True,
        packages=vars['packages'],
        install_requires=requirements,
        classifiers=[
            'Operating System :: OS Independent',
            'Programming Language :: Python',
        ],
        url='https://github.com/seonsfx/serverless-python',
    )
