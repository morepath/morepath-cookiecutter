# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

name = '{{ cookiecutter.package_name }}'
description = (
    '{{ cookiecutter.description }}'
)
version = '0.0.0'


setup(
    name=name,
    version=version,
    description=description,
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.author_email }}',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=name.split('.')[:-1],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        {% if 'REST' in cookiecutter.goal %}'morepath'
        {%- endif -%}
        {% if 'traditional' in cookiecutter.goal -%}
        'morepath',
        'more.chameleon',
        {%- endif %}
    ],
    extras_require=dict(
        test=[
            'pytest',
            'webtest',
        ],
    ),
    entry_points=dict(
        console_scripts=[
            'run-app = {{ cookiecutter.package_name }}.run:run',
        ],
    ),
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ]
)
