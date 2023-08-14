import click
from tools.commands.cli import cli
# from sysit.common_imports import *

def main():
    """Main entry point for the application script"""
    click.echo("sysit is running... \n")

    # add any initalization code here

    #run the Click-based CLI commands defined in cli.py
    cli()

if __name__ == "__main__":
    main()

