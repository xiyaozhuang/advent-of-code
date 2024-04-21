import pytest
import re
import os
import shutil

from advent_of_code import year_0000, year_2015
from advent_of_code.scripts.utils import load_data, get_callables


@pytest.fixture
def write_tmp_data():
    modules = (year_0000, year_2015)
    status = (1, 2)
    data_path = "data/tmp"

    years = (re.search(r"\d+", module.__name__).group() for module in modules)

    for year in years:
        for n_days in status:
            for day in range(1, n_days + 1):
                filename = f"{data_path}/{year}/{day}.txt"
                os.makedirs(os.path.dirname(filename), exist_ok=True)

                with open(filename, "w+") as file:
                    file.write(f"day {day}")

    yield modules, status, data_path

    shutil.rmtree(data_path)


def test_load_data(write_tmp_data):
    modules, status, data_path = write_tmp_data

    input = data_path
    expected = {
        "0000/1": {"module": year_0000, "data": "day 1"},
        "2015/1": {"module": year_2015, "data": "day 1"},
        "2015/2": {"module": year_2015, "data": "day 2"},
    }
    output = load_data(modules, status, input)

    assert output == expected


def test_get_callables():
    input = (year_0000, year_0000.Day1, year_0000.Day2)
    expected = [
        year_0000.Day1,
        year_0000.Day2,
        year_0000.Day1.part_1,
        year_0000.Day1.part_2,
        year_0000.Day2.part_1,
        year_0000.Day2.part_2,
    ]
    output = []

    for item in input:
        output += get_callables(item)

    assert output == expected
