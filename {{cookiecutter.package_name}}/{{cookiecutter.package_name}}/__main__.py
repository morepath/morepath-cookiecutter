import morepath
from .app import App


def run():
    morepath.autoscan()
    morepath.run(App())


if __name__ == '__main__':
    run()
