#!/usr/bin/env python

from setuptools import setup, find_packages

desc = ''
with open('README.md') as f:
    desc = f.read()

setup(
    name='tx-api',
    version='0.1.0',
    description=('Enumbra Transaction API'),
    long_description=desc,
    url='https://github.com/cyberaa',
    author='João Jesus',
    author_email='exceltior@gmail.com',
    license='Apache v2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='api',
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),
    install_requires=[
        'falcon>=1.1.0',
        'gunicorn>=19.7.1',
        'docopt>=0.6.2',
        'jsonschema>=2.6.0',
        'mysql-connector>=2.1.6',
        'PyMySQL>=0.8.0',
        'aumbry>=0.7.0',
        'SQLAlchemy>=1.2.4',
        'aumbry[yaml]>=0.2.0'
    ],
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [
            'tx-api = transactions_api.__main__:main'
        ],
    },
)