from pathlib import Path
import day_1_service as ms

path = Path(__file__).parent.parent
fileName = 'input.txt'
inputFile = path / fileName

with open(inputFile, 'r') as f:
    measures = f.readlines()

measures = [int(measure.strip()) for measure in measures]

print("--- Day One ---")

print("--- Part One ---", ms.get_number_magnifications_measurements(measures))

print("--- Part Two ---", ms.get_number_magnifications_three_measurements(measures))

fileName = 'input_day_2.txt'
inputFile = path / fileName

with open(inputFile, 'r') as f:
    positions = f.readlines()

print("--- Day Two ---")
print("--- Part One ---", ms.get_final_position(positions))
