{{ cookiecutter.package_name.split('.') | map('capitalize') | join(' ') }}
{{ "=" * cookiecutter.package_name.__len__() }}

{{ cookiecutter.description }}

Run the Tests
-------------

Install tox and run it::

    pip install tox
    tox

Limit the tests to a specific python version::

    tox -e py27
