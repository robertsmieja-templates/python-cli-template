import click


@click.command()
@click.option('--name', default="world", help="Name to use when printing 'hello'")
def main(name):
    click.echo("Hello %s" % name)


if __name__ == "__main__":
    main()
