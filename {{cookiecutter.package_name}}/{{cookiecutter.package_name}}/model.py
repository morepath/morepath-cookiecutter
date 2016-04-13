class Root(object):
    @property
    def greetings(self):
        return [
            Greeting('mundo'),
            Greeting('world')
        ]


class Greeting(object):
    def __init__(self, person):
        self.person = person
