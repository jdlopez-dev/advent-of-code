import sys
from day_1_models import Position


def get_number_magnifications_measurements(measures):
    previous_measurement = sys.maxsize
    measurement_counter = 0
    for measure in measures:
        if measure > previous_measurement:
            measurement_counter += 1
        previous_measurement = measure
    return measurement_counter


def get_number_magnifications_three_measurements(measures):
    previous_measurement = sys.maxsize
    measurement_counter = 0
    measures_len = len(measures)
    for i in range(measures_len):
        if(i + 2 < measures_len):
            current_measure = measures[i] + measures[i + 1] + measures[i + 2]
            if current_measure > previous_measurement:
                measurement_counter += 1
            previous_measurement = current_measure
    return measurement_counter


def get_final_position(positions):

    horizontal_position = 0
    depth = 0

    for position in positions:
        if(Position.forward.name in position):
            horizontal_position += int(position.split()[1])
        elif(Position.down.name in position):
            depth += int(position.split()[1])
        elif(Position.up.name in position):
            depth -= int(position.split()[1])

    final_result = horizontal_position * depth
    return final_result
