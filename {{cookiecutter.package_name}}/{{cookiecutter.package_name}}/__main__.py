import morepath
from .app import App


def run():
    morepath.autosetup()
    morepath.run(App())
