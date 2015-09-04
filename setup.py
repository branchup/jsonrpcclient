"""setup.py"""
#pylint:disable=line-too-long

from codecs import open as codecs_open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup #pylint:disable=import-error,no-name-in-module

with codecs_open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

with codecs_open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name='jsonrpcclient',
    version='2.0.1',
    description='JSON-RPC client library.',
    long_description=readme + '\n\n' + history,
    author='Beau Barker',
    author_email='beauinmelbourne@gmail.com',
    url='https://jsonrpcclient.readthedocs.org/',
    packages=['jsonrpcclient'],
    package_data={'jsonrpcclient': ['response-schema.json']},
    include_package_data=True,
    install_requires=['jsonschema', 'future', 'requests', 'pyzmq'],
    tests_require=['tox'],
    classifiers=[
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        ],
    )
