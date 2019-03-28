# -*- coding: utf-8 -*-

# Import modified 'os' module with LC_LANG set so click doesn't complain
from .os_utils import os  # noqa: F401

import click

settings = dict(help_option_names=['-h', '--help'])

from python_boilerplate_test01.hello import hello



@click.group(options_metavar='', hello_metavar='<command>',
             context_settings=settings)
def cli():
    """
    Python Boilerplate contains all the boilerplate you need to create a Python package.
    """
    pass


cli.add_command(hello, name='hello')


if __name__ == "__main__":
    cli()
