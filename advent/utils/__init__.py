# SPDX-License-Identifier: GPLv3
# SPDX-FileCopyrightText: 2023 Helio Chissini de Castro
from __future__ import annotations

import logging as stdlogger

from rich.logging import RichHandler

# Setup the main logger message
stdlogger.basicConfig(level="INFO", format="%(message)s", datefmt="[%X]", handlers=[RichHandler(markup=True)])

# Global log variable
logging = stdlogger.getLogger("rich")


def set_log_level(level: str = "INFO") -> None:
    logging.setLevel(level=level)
