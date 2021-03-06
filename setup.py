from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='tservice',
    version='1.1.0dev',
    description=(
        'Start a local Tornado static file server'),
    long_description=long_description,
    author='Matt Davis',
    author_email='jiffyclub@gmail.com',
    url='https://github.com/jiffyclub/tservice',
    packages=find_packages(),
    install_requires=['tornado >= 4.0'],
    entry_points={
        'console_scripts': ['tserve = tservice.cli:main']},
    tests_require=['requests >= 2.0'],
    classifiers=[
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'])
