# SPDX-License-Identifier: GPLv3
# SPDX-FileCopyrightText: 2023 Helio Chissini de Castro

from __future__ import annotations

from pathlib import Path

import pytest

from advent.days import day1
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

    return load_data("day1_testdata")


@pytest.fixture
def test_data2() -> list[str]:
    """Fixture of test data

    Returns:
        _type_: List of data
    """

    return load_data("day1_testdata2")


def test_calibration(test_data: list[str]) -> None:
    """Test Day 1 - Calibration"""
    day = day1.Day()
    day.data = test_data
    day.process()

    if not day.result == 142:
        raise ValueError(f"Expected result 142. Got {day.result}")


def test_calibration2(test_data2: list[str]) -> None:
    """Test Day 1 - Calibration2"""
    set_log_level("DEBUG")
    day = day1.Day()
    day.data = test_data2
    day.process()

    if not day.result == 281:
        raise ValueError(f"Expected result 142. Got {day.result}")
