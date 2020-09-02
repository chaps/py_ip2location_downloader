#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Chaps SD",
    author_email='drumchaps@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Package to download IP2Location resources",
    entry_points={
        'console_scripts': [
            'py_ip2location_downloader=py_ip2location_downloader.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='py_ip2location_downloader',
    name='py_ip2location_downloader',
    packages=find_packages(include=['py_ip2location_downloader', 'py_ip2location_downloader.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    license="MIT license",
    url='https://github.com/chaps/py_ip2location_downloader',
    version='0.1.0',
    zip_safe=False,
)
