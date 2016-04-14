¨# A Cookiecutter Template for Morepath

A cookiecutter template to get started with [Morepath](https://morepath.readthedocs.org),
based on the [organizing your project](http://morepath.readthedocs.org/en/latest/organizing_your_project.html)
chapter from the Morepath documentation.

This template either generates a RESTful application or a tradiational web
application (HTML). The wizard will ask you to choose between those two
options.

If you go with the traditional route, the [Chameleon templating language](https://chameleon.readthedocs.org/en/latest/)
will be used. Feel free to switch to another templating language. We've chosen
one for you because adding support for multiple templating languages would make
this cookiecutter template quite messy.

# Requirements

To use this template, install the latest version of cookiecutter:

    pip install --upgrade cookiecutter

You will also need Python 2.7 or 3.3+ and [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

# Usage

Create a new package with the wizard:

    cookiecutter https://github.com/morepath/morepath-cookiecutter

(The result will be stored in a new directory named after the package)

Inside the so created package create a virtualenv:

    cd my-package
    virtualenv env
    source env/bin/activate

And install the package (including tests):

    env/bin/pip install -e '.[test]'

You can now run your application using the following command:

    env/bin/run-app

Once the application is running you can open it in your browser under
[http://localhost:5000](http://localhost:5000).

There is also one example test included which you can run using:

    env/bin/py.test

# Features

This template is pretty bare-bones. We do not offer support for various
integrations like travis-ci or tox, because we mean to help out beginners
with Morepath.

If you require more advanced features, feel free to fork!

# Structure

In the resulting directory you find the following files:

* `./app.py`: Contains the Morepath application.
* `./model.py`: Contains the models you are working with.
* `./path.py`: Contains the paths pointing to the models.
* `./view.py`: Contains the views associated with the models.
* `./run.py`: Contains the run script for the test server.
* `./tests/test_app.py`: Contains an example test.

# License

The Cookiecutter Template for Morepath is released into the public domain.

# More Information

* https://morepath.readthedocs.org
* https://github.com/audreyr/cookiecutter
