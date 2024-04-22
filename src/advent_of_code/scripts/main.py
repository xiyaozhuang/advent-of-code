from advent_of_code.scripts.config import modules, status, data_path
from advent_of_code.scripts.utils import load_data, get_solutions

data = load_data(modules, status, data_path)
solutions = get_solutions(data)

print("Solutions:")
for key, value in solutions.items():
    print(f"{key}: {value}")
