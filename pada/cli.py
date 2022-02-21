# -*- coding: utf-8 -*-
import click
from stacklog import stacklog

from pada import __version__ as version

@click.group()
@click.version_option(version)
@click.option('-v', '--verbose',
              count=True,
              help='Increase verbosity')
@click.option('-q', '--quiet',
              count=True,
              help='Decrease verbosity'
              )
def cli(verbose, quiet):
    pass


@cli.command()
@stacklog(click.echo, 'Generating new PADA project')
def create():
    # create a project
    import pada.templating
    pada.templating.render_project_template()


