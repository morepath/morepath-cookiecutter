import morepath
import {{ cookiecutter.package_name }}

from webtest import TestApp as Client


def test_root():
    morepath.scan({{ cookiecutter.package_name }})
    morepath.commit({{ cookiecutter.package_name }}.App)

    client = Client({{ cookiecutter.package_name }}.App())
    root = client.get('/')

    assert root.status_code == 200
    {%- if 'traditional' in cookiecutter.goal %}
    assert '/greeting/world' in root
    assert '/greeting/mundo' in root
    {%- else %}
    assert len(root.json['greetings']) == 2
    {%- endif %}
