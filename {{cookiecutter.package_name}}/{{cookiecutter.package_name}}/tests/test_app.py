import morepath
import {{ cookiecutter.package_name }}

from webtest import TestApp as Client


def test_redirect():
    morepath.scan({{ cookiecutter.package_name }})
    morepath.commit({{ cookiecutter.package_name }}.App)

    client = Client({{ cookiecutter.package_name }}.App())
    root = client.get('/')

    assert root.status_code == 302
    assert root.location.endswith('greeting/world')
