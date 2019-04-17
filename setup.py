
#!/usr/bin/env python

# Copyright (C) 2019 SignalFx, Inc. All rights reserved.

import sys
from setuptools import setup, find_packages

if '--module' in sys.argv:
    idx = sys.argv.index('--module')
    sys.argv.pop(idx)
    module = sys.argv.pop(idx)

    vars = {}

    with open(module + '/version.py') as f:
        exec(f.read(), vars)

    with open('README.rst') as readme:
        long_description = readme.read()

    with open('requirements.txt') as f:
        requirements = [line.strip() for line in f.readlines()]

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
        url='https://github.com/signalfx/serverless-python',
    )
else:
    print("Missing parameter : --module")
