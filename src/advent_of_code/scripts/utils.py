import re


def load_data(modules, status, data_path):
    output = {}
    years = [re.search(r"\d+", module.__name__).group() for module in modules]

    for i in range(len(years)):
        year = years[i]
        module = modules[i]
        end = status[i] + 1

        for day in range(1, end):
            with open(f"{data_path}/{year}/{day}.txt") as file:
                data = file.read()

            output[f"{year}/{day}"] = {"module": module, "data": data}

    return output


def get_callables(obj):
    return [getattr(obj, attr) for attr in dir(obj) if attr.startswith(("Day", "part"))]


def get_solutions(input):
    output = {}

    keys = list(input.keys())

    for i in range(len(keys)):
        key = keys[i]

        module = input[key]["module"]
        class_obj = get_callables(module)[i]
        methods = get_callables(class_obj)

        for j in range(len(methods)):
            data = input[key]["data"]
            method = methods[j]
            output[f"{key}/part_{j + 1}"] = method(data)

    return output
