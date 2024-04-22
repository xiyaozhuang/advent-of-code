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
