# SPDX-License-Identifier: GPLv3
# SPDX-FileCopyrightText: 2023 Helio Chissini de Castro

from __future__ import annotations

from advent.base import Base
from advent.utils import logging

"""
--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you
a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by
December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second
puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you
("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the
sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a
trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been
amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are
having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration
value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit
and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one,
two, three, four, five, six, seven, eight, and nine also count as valid "digits".
"""


class Day(Base):
    """
    Day 1 implementation
    """

    result: int = 0

    def process(self) -> None:
        if not self.data:
            return
        for entry_line in self.data:
            entry = self.transform_text_in_digit(entry_line)
            value: int = int(f"{self.get_digit(entry)}{self.get_digit(entry, True)}")
            logging.debug(f"Current value: {value}")
            self.result = self.result + value

        logging.info(f"Current output: {self.result}")

    def get_digit(self, entry: str, reverse: bool = False) -> str:
        return next(x for x in entry if x.isdigit()) if not reverse else next(x for x in reversed(entry) if x.isdigit())

    def transform_text_in_digit(self, entry: str) -> str:
        numbers: list[tuple[str, str]] = [
            ("one", "1"),
            ("two", "2"),
            ("three", "3"),
            ("four", "4"),
            ("five", "5"),
            ("six", "6"),
            ("seven", "7"),
            ("eight", "8"),
            ("nine", "9"),
        ]
        for pos in range(0, len(entry)):
            data = next((x for x in numbers if entry[pos:].startswith(x[0])), None)
            if data:
                entry = entry.replace(data[0], data[1])
                break
        print(entry)
        reversed_entry = entry[::-1]
        for pos in range(0, len(reversed_entry)):
            data = next((x for x in numbers if reversed_entry[pos:].startswith(x[0][::-1])), None)
            if data:
                entry = entry.replace(data[0], data[1])
                break
        print(entry)
        return entry
