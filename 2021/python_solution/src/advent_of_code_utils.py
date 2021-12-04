from pathlib import Path

def print_day(day_number, part_one, part_two):
    print("--- Day " + str(day_number) + " ---")
    print("Part One: ", part_one)
    print("Part Two: ", part_two)

def get_data(file_name):
    path = Path(__file__).parent.parent / 'data'

    input_file = path / file_name

    with open(input_file, 'r') as f:
        data = f.readlines()
    return data