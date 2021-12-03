import sys


def get_number_magnifications_measurements(measures):
    previous_measurement = sys.maxsize
    measurement_counter = 0
    for measure in measures:
        if measure > previous_measurement:
            measurement_counter += 1
        previous_measurement = measure
    return measurement_counter