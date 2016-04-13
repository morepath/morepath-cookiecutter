from .app import App
from . import model


{%- if 'REST' in cookiecutter.goal %}


@App.json(model=model.Root)
def view_root(self, request):
    return {
        'greetings': [
            {
                'name': greeting.person,
                'url': request.link(greeting)
            }
            for greeting in self.greetings
        ]
    }


@App.json(model=model.Greeting)
def view_greeting(self, request):
    return {
        'greeting': 'hello ' + self.person
    }
{%- else %}


@App.html(model=model.Root, template='index.pt')
def view_root(self, request):
    return {
        'greetings': self.greetings,
        'request': request,
    }


@App.html(model=model.Greeting, template='greeting.pt')
def view_greeting(self, request):
    return {
        'greeting': 'hello ' + self.person
    }
{%- endif %}
