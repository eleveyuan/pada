import click
from stacklog import stacklog

from bricks import __version__ as version

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


@click.command()
@stacklog(click.echo, 'Generating new bricks project')
def create():
    # create a project
    import bricks.templating
    bricks.templating.render_project_template()


cli.add_command(create)


if __name__ == '__main__':
    cli()
