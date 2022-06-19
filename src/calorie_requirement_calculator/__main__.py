"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Calorie Requirement Calculator."""


if __name__ == "__main__":
    main(prog_name="calorie-requirement-calculator")  # pragma: no cover
