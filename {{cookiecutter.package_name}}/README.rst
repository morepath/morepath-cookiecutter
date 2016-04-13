{{ cookiecutter.package_name.split('.') | map('capitalize') | join(' ') }}
{{ "=" * cookiecutter.package_name.__len__() }}

{{ cookiecutter.description }}
