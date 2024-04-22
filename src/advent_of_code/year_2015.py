import numpy as np


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
    def part_1(moves):
        distance = len(moves)
        n = 2 * distance + 1

        grid = np.zeros((n, n), dtype=int)
        row, col = distance, distance
        grid[row, col] = 1

        for move in moves:
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

        return np.sum(grid)
