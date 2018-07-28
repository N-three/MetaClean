import click

@click.command()
@click.argument('files', nargs=-1, type=click.Path())
# @click.option('--recursive', '-r', default=False, type=bool)
def cli(files):
    for file in files:
        click.echo(file)

    # TODO: Set up arguments and start core with given files and settings