from pathlib import Path
import day_1_service as ms

fileName = 'input.txt'
path = Path(__file__).parent.parent
inputFile = path / fileName


with open(inputFile, 'r') as f:
    measures = f.readlines()

measures = [int(measure.strip()) for measure in measures]

print("--- Part One ---", ms.get_number_magnifications_measurements(measures))

print("--- Part Two ---", ms.get_number_magnifications_three_measurements(measures))
