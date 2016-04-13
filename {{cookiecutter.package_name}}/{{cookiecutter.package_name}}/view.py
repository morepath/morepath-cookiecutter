import morepath

from .app import App
from . import model


@App.view(model=model.Root)
def view_root(self, request):
    return morepath.redirect(request.link(model.Greeting('world')))

{%- if 'REST' in cookiecutter.goal %}

@App.json(model=model.Greeting)
def view_greeting(self, request):
    return {
        'greeting': 'hello ' + self.person
    }
{%- else %}

@App.html(model=model.Greeting, template='greeting.pt')
def view_greeting(self, request):
    return {
        'greeting': 'hello ' + self.person
    }
{%- endif %}
