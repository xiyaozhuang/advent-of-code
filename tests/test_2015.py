from advent_of_code.year_2015 import *


class TestDay1:
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


class TestDay2:
    def test_part_1(self):
        input = "2x3x4\n1x1x10"
        expected = 58 + 43
        output = Day2.part_1(input)

        assert output == expected

    def test_part_2(self):
        input = "2x3x4\n1x1x10"
        expected = 34 + 14
        output = Day2.part_2(input)

        assert output == expected


class TestDay3:
    def test_part_1(self):
        input = [">", "^>v<", "^v^v^v^v^v"]
        expected = [2, 4, 2]
        output = [Day3.part_1(item) for item in input]

        assert output == expected

    def test_part_2(self):
        input = ["^v", "^>v<", "^v^v^v^v^v"]
        expected = [3, 3, 11]
        output = [Day3.part_2(item) for item in input]

        assert output == expected


class TestDay4:
    def test_part_1(self):
        input = ["abcdef", "pqrstuv"]
        expected = [609043, 1048970]
        output = [Day4.part_1(item) for item in input]

        assert output == expected

    def test_part_2(self):
        input = ["abcdef", "pqrstuv"]
        expected = [6742839, 5714438]
        output = [Day4.part_2(item) for item in input]

        assert output == expected


class TestDay5:
    def test_part_1(self):
        input = "ugknbfddgicrmopn\naaa\njchzalrnumimnmhp\nhaegwjzuvuyypxyu\ndvszwmarrgswjxmb\n"
        expected = 2
        output = Day5.part_1(input)

        assert output == expected

    def test_part_2(self):
        input = "qjhvhtzxzqqjkmpb\nxxyxx\nuurcxstgmygtbstg\nieodomkazucvgmuy\n"
        expected = 2
        output = Day5.part_2(input)

        assert output == expected


class TestDay6:
    def test_part_1(self):
        input = "turn on 0,0 through 999,999\ntoggle 0,0 through 999,0\nturn off 499,499 through 500,500\n"
        expected = 1000000 - 1000 - 4
        output = Day6.part_1(input)

        assert output == expected

    def test_part_2(self):
        input = "turn on 0,0 through 0,0\ntoggle 0,0 through 999,999\n"
        expected = 1 + 2000000
        output = Day6.part_2(input)

        assert output == expected
