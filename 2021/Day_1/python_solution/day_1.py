from pathlib import Path
import measurement_service as ms

fileName = 'input.txt'
path = Path(__file__).parent.parent
inputFile = path / fileName


with open(inputFile, 'r') as f:
    measures = f.readlines()

measures = [int(measure.strip()) for measure in measures]

print(ms.get_number_magnifications_measurements(measures))
