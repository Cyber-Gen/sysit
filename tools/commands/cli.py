import click
from sysit.os_linux import *
from sysit.os_windows import *
from sysit.os_macos import *
from sysit.sys_checks import check_os, check_dns_config, check_ping, check_ip, check_dns_config

@click.group()
def cli():
    " The AWEsome CLI for Sysit "
    pass

@cli.command()
# @click.option("-p", "--param", help="This change some text")
def c1():
    """Check the OS type"""
    click.echo("Checking OS type...\n")
    check_os()

@cli.command()
def c2():
    """Check network status"""
    click.echo("Checking ping status...\n")
    check_ping()

# lets define all functions for imported check modules
@cli.command()
def c3():
    """Check public IP address"""
    click.echo("Checking public IP address...\n")
    check_ip()

@cli.command()
def c4():
    """Check system's DNS resolver configuration"""
    click.echo("Checking system's DNS resolver configuration...\n")
    check_dns_config()


if __name__ == "__main__":
    cli()