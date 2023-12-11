# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

"""
Advennt of Code Base utility functions

As per default regular input on all Advent of Code commits comes in txt format,
make standard base class always ready the related input in txt format
"""
from __future__ import annotations

import sys
from pathlib import Path

from advent.utils import logging


class Base:
    """
    Base Class - Utility Functions
    """

    def __init__(self, filename: Path | None = None):
        self.data: list[str]
        if filename:
            self.readdata(filename)

    def readdata(self, filename: Path) -> None:
        """
        Read a text input data file

        Args:
            filename (str): the filename path
        """
        logging.debug(f"Attempt to load resource file {filename.as_posix()}")
        try:
            # pylint: disable=unspecified-encoding
            with filename.open() as inputfile:
                self.data = [entry.rstrip() for entry in inputfile]
        except OSError:
            print("Input file could not be found.")
            sys.exit(1)
