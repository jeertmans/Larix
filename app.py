import click
import os
from larix import *

VERSION = "0.1a1"

def listfiles(directory):
    return [file for file in os.listdir(directory) if os.path.isfile(file)]


def files_callback(ctx, param, value):
    if not value:
        files = tuple(input().split(" "))
        for file in files:
            if not os.path.exists(file):
                raise click.BadParameter(f"Path '{file}' does not exist", ctx=ctx, param=None)
        value = files

    return value


@click.command()
@click.option("--jobs", "-n", type=int, default=0, help="Split the task into (max.) n parallel jobs.")
@click.option("--verbose", "-v", is_flag=True, help="Add verbosity to ouput.")
@click.option("--version", is_flag=True, help="Print current Larix version and exit.")
@click.argument("files", nargs=-1, type=click.Path(exists=True), autocompletion=listfiles("."), callback=files_callback)
def main(n, verbose, version, files):
    """
    Larix constructs a file dependency network from input files.
    This is especially interesting when working on large projects.

    Basic usage only requires one input file, i.e., the `main`, since all the dependencies will be detected.

    Inputs files can also be piped, e.g. `echo "app.py" | larix`.
    """
    click.echo("main")
    if version:
        click.echo(VERSION)
        exit(0)

        
    print(files)
    for file in files:
        process_file(file)
if __name__ == '__main__':
    click.echo("lol")
