"""Command-line entry point. Phase 9 replaces argparse with Typer subcommands."""
import argparse

from forecast import __version__


def main() -> None:
    parser = argparse.ArgumentParser(prog="forecast", description="Probabilistic forecasting lab")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.parse_args()
    parser.print_help()