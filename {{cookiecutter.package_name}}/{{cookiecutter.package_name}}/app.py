import morepath
{% if 'traditional' in cookiecutter.goal -%}from more.chameleon import ChameleonApp{%- endif -%}

{% if 'REST' in cookiecutter.goal %}

class App(morepath.App):
    pass
{% else %}

class App(ChameleonApp):
    pass

@App.template_directory()
def get_template_directory():
    return 'templates'

@App.setting_section(section='chameleon')
def get_chameleon_settings():
    return {'debug': True}
{% endif %}
