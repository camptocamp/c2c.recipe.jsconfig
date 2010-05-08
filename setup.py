# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

entry_point = 'c2c.recipe.jsconfig:Recipe'

setup(
    name             = 'c2c.recipe.jsconfig',
    version          = '0.1',
    description      = 'Generate a javascript configuration file based on buildout configuration',
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    author           = 'Bruno Binet',
    author_email     = 'bruno.binet@camptocamp.com',
    url              = 'http://github.com/camptocamp/c2c.recipe.jsconfig',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['c2c', 'c2c.recipe'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools',
                      'zc.buildout',
                      ],
    entry_points     = {'zc.buildout' : ['default = %s' %entry_point]},
)
