import morepath
from .app import App


def run():
    morepath.autosetup()
    morepath.run(App())


if __name__ == '__main__':
    run()
