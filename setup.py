# encoding: utf-8
from setuptools import setup, find_packages


setup(
    name = 'ms-processing',
    version = "0.1.0",
    description = '',
    author = u'Pablo Calvo',
    author_email = 'pablo.calvo.velilla@everis.com',
    zip_safe=False,
    include_package_data = True,
    packages = find_packages(exclude=[]),
    install_requires=[
        'bottle==0.12.09',
        'eurekalab==0.1.0',
        'nose==1.3.7',
        'mock==1.3.0'
    ]
)
