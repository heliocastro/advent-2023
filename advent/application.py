# SPDX-License-Identifier: GPLv3
# SPDX-FileCopyrightText: 2023 Helio Chissini de Castro

from __future__ import annotations

import importlib
from pathlib import Path

import click

from advent.utils import logging


@click.group()
def messages() -> None:
    """Help messages stub"""


@click.command()
@click.argument("day_of_month", type=click.INT)
@click.option("-d", "--debug", type=bool, is_flag=True, default=False, help="Enable debug information")
@click.option("-f", "--filename", "filename")
def day(day_of_month: int, debug: bool, filename: Path | None = None) -> None:
    """Do Day Work"""
    if debug:
        logging.setLevel("DEBUG")

    module = f"advent.days.day{day_of_month}"
    day_module = importlib.import_module(module)
    if not filename:
        file: Path = Path(__file__).parent / f"days/resources/day{day_of_month}.txt"
    day_chore = day_module.Day(file)
    day_chore.process()


messages.add_command(day)


if __name__ == "__main__":
    messages()
