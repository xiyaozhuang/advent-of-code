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
