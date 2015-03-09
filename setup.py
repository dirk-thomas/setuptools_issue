from setuptools import find_packages
from setuptools import setup

setup(
    name='foo',
    version='1.0.0',
    packages=find_packages(),
    scripts=['bin/test_foo'],
    install_requires=['setuptools'],
    author='Dirk Thomas',
    author_email='dthomas@osrfoundation.org',
    maintainer='Dirk Thomas',
    maintainer_email='dthomas@osrfoundation.org',
    url='https://github.com/dirk-thomas/setuptools_issue',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Example to demonstrate setuptools issue.',
    license='Apache License, Version 2.0',
    entry_points={
        'foo.entrypoints': [
            'foo = foo',
        ],
    },
    zip_safe=False,
)
