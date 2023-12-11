# SPDX-License-Identifier: GPLv3
# SPDX-FileCopyrightText: 2023 Helio Chissini de Castro

from __future__ import annotations

from pathlib import Path

import pytest

from advent.days import day2
from advent.utils import set_log_level


def load_data(test: str) -> list[str]:
    """Read test data"""
    data_file: Path = Path(Path(__file__).parent / f"resources/{test}.txt")
    with data_file.open() as file:
        data: list[str] = file.readlines()

    return data


@pytest.fixture
def test_data() -> list[str]:
    """Fixture of test data

    Returns:
        _type_: List of data
    """

    return load_data("day2_testdata")


def test_cubes(test_data: list[str]) -> None:
    """Test Day 2 - Cubes"""
    set_log_level("DEBUG")
    day = day2.Day()
    day.data = test_data
    valid_games, powers_sum = day.games(red=12, green=13, blue=14)

    if not valid_games == 8:
        raise ValueError(f"Expected result 8. Got {valid_games}")

    if not powers_sum == 2286:
        raise ValueError(f"Expected result 2286. Got {powers_sum}")
