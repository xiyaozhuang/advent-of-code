from advent_of_code.year_2015 import *


class TestDayOne:
    def test_part_1(self):
        input = ("(())", "(((", "))(((((", "())", ")))")
        expected = [0, 3, 3, -1, -3]
        output = [Day1.part_1(item) for item in input]

        assert output == expected

    def test_part_2(self):
        input = ("))", "()())")
        expected = [1, 5]
        output = [Day1.part_2(item) for item in input]

        assert output == expected
