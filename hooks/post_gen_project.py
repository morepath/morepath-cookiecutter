#!/bin/python
import os
import shutil

from contextlib import contextmanager


@contextmanager
def switch_directory(path):
    previous_path = os.getcwd()

    os.chdir(path)
    yield
    os.chdir(previous_path)


def get_parent_directory(path):
    return os.path.split(path)


def get_directory_name(path):
    return os.path.split(path)[-1]


def create_nested_folders(package_name, target):

    declare_ns = "__import__('pkg_resources').declare_namespace(__name__)\n"

    # make sure to get back to the original cwd
    with switch_directory(os.getcwd()):
        parts = package_name.split('.')

        for ix, part in enumerate(parts):
            if (ix + 1) == len(parts):
                shutil.move(target, part)
            else:
                os.mkdir(part)
                os.chdir(part)

                with open('__init__.py', 'w') as f:
                    f.write(declare_ns)


# create nested package folders (my.package becomes my/package)
package_name = get_directory_name(os.getcwd())

if '.' in package_name:
    create_nested_folders(
        package_name=package_name,
        target=os.path.join(os.getcwd(), package_name)
    )

# remove templates dir if REST application was requested
goal = '{{ cookiecutter.goal }}'

if 'REST' in goal:
    parts = [os.getcwd()]
    parts.extend(package_name.split('.'))
    parts.append('templates')

    shutil.rmtree(os.path.join(*parts))
