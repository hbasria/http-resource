#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='http-resource',
    version='0.1.4',
    description='http resource',
    long_description=long_description,
    author='Hasan Basri',
    author_email='hbasria@gmail.com',
    license='MIT',
    keywords='http resource',
    url='https://github.com/hbasria/http-resource',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['six>=1.11.0',
                      'requests>=2.18.3',
                      'py_dictutils>=0.1.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    test_suite='tests'
)
