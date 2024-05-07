import numpy as np
from hashlib import md5
import re


class Day1:
    def part_1(string):
        floor = 0

        for char in string:
            if char == "(":
                floor += 1

            else:
                floor -= 1

        return floor

    def part_2(string):
        floor = 0

        for i in range(len(string)):
            if string[i] == "(":
                floor += 1

            else:
                floor -= 1

            if floor == -1:
                return i + 1


class Day2:
    def part_1(string):
        presents = string.splitlines()
        total = 0

        for dimensions in presents:
            l, w, h = map(int, dimensions.split("x"))
            areas = (l * w, w * h, h * l)
            surface_area = 2 * sum(areas)

            total += surface_area + min(areas)

        return total

    def part_2(string):
        presents = string.splitlines()
        total = 0

        for dimensions in presents:
            l, w, h = map(int, dimensions.split("x"))
            perimeters = (2 * (l + w), 2 * (w + h), 2 * (h + l))
            volume = l * w * h

            total += min(perimeters) + volume

        return total


class Day3:
    def update_grid(grid, row, col, move):
        if move == "^":
            grid[row - 1, col] = 1
            row -= 1

        elif move == "v":
            grid[row + 1, col] = 1
            row += 1

        elif move == "<":
            grid[row, col - 1] = 1
            col -= 1
        else:
            grid[row, col + 1] = 1
            col += 1

        return row, col

    def part_1(moves):
        distance = len(moves)
        n = 2 * distance + 1

        grid = np.zeros((n, n), dtype=int)
        row, col = distance, distance
        grid[row, col] = 1

        for move in moves:
            row, col = Day3.update_grid(grid, row, col, move)

        return np.sum(grid)

    def part_2(moves):
        distance = len(moves)
        n = 2 * distance + 1

        grid_santa = np.zeros((n, n), dtype=int)
        grid_robot = np.zeros((n, n), dtype=int)
        row_santa, col_santa = distance, distance
        row_robot, col_robot = distance, distance
        grid_santa[row_santa, col_santa] = 1
        grid_robot[row_robot, col_robot] = 1

        turn = 0

        for move in moves:
            if turn % 2 == 0:
                row_santa, col_santa = Day3.update_grid(
                    grid_santa, row_santa, col_santa, move
                )

            else:
                row_robot, col_robot = Day3.update_grid(
                    grid_robot, row_robot, col_robot, move
                )

            turn += 1

        return np.count_nonzero(grid_santa + grid_robot)


class Day4:
    def search_md5(string, prefix):
        hash_md5 = md5(string.encode()).hexdigest()
        n = 0

        while not hash_md5.startswith(prefix):
            n += 1
            new_string = string + str(n)
            hash_md5 = md5(new_string.encode()).hexdigest()

        return n

    def part_1(string):
        return Day4.search_md5(string, "00000")

    def part_2(string):
        return Day4.search_md5(string, "000000")


class Day5:
    def naughty_or_nice(string, *conditions):
        strings = string.splitlines()
        total = 0

        for item in strings:
            if all([condition(item) for condition in conditions]):
                total += 1

        return total

    def part_1(string):
        condition1 = lambda x: sum([char in "aeiou" for char in x]) > 2
        condition2 = lambda x: bool(re.search(r"(.)\1", x))
        condition3 = lambda x: not bool(re.search("ab|cd|pq|xy", x))

        return Day5.naughty_or_nice(string, condition1, condition2, condition3)

    def part_2(string):
        condition1 = lambda x: bool(re.search(r"(..).*\1", x))
        condition2 = lambda x: bool(re.search(r"(.).\1", x))

        return Day5.naughty_or_nice(string, condition1, condition2)


class Day6:
    def part_1(string):
        instructions = string.splitlines()
        grid = np.zeros((1000, 1000), dtype=int)

        for instruction in instructions:
            start_x, start_y, end_x, end_y = map(int, re.findall(r"\d+", instruction))

            if "turn on" in instruction:
                grid[start_x : end_x + 1, start_y : end_y + 1] = 1

            elif "turn off" in instruction:
                grid[start_x : end_x + 1, start_y : end_y + 1] = 0

            else:
                grid[start_x : end_x + 1, start_y : end_y + 1] = (
                    1 - grid[start_x : end_x + 1, start_y : end_y + 1]
                )

        return grid.sum()
