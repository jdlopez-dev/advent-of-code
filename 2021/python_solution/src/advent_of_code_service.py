import sys
from advent_of_code_models import Position
from collections import Counter


def get_number_magnifications_measurements(data):
    measures = [int(measure.strip()) for measure in data]
    previous_measurement = sys.maxsize
    measurement_counter = 0
    for measure in measures:
        if measure > previous_measurement:
            measurement_counter += 1
        previous_measurement = measure
    return measurement_counter


def get_number_magnifications_three_measurements(data):
    measures = [int(measure.strip()) for measure in data]
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
        value = int(position.split()[1])
        if(Position.forward.name in position):
            horizontal_position += value
        elif(Position.down.name in position):
            depth += value
        elif(Position.up.name in position):
            depth -= value

    final_result = horizontal_position * depth
    return final_result


def get_final_position_with_aim(positions):

    horizontal_position = 0
    depth = 0
    aim = 0

    for position in positions:
        value = int(position.split()[1])
        if(Position.forward.name in position):
            horizontal_position += value
            depth += value * aim
        elif(Position.down.name in position):
            aim += value
        elif(Position.up.name in position):
            aim -= value

    final_result = horizontal_position * depth
    return final_result


def get_power_consumption(data):
    gamma_rate = 0
    epsilon_rate = 0
    inverse_binary_numbers = []

    for binary_number_index in range(0, len(data)):
        binary_number_split = list(data[binary_number_index].strip())
        for i in range(0, len(binary_number_split)):
            if(i < len(inverse_binary_numbers)):
                inverse_binary_numbers[i] += binary_number_split[i]
            else:
                inverse_binary_numbers.append(binary_number_split[i])

    temp_epsilon_rate = ''
    temp_gamma_rate = ''

    for i in range(0, len(inverse_binary_numbers)):
        list_counter = Counter(list(inverse_binary_numbers[i]))

        temp_epsilon_rate += list_counter.most_common()[0][0]
        temp_gamma_rate += list_counter.most_common()[1][0]

    gamma_rate = int(temp_gamma_rate, 2)
    epsilon_rate = int(temp_epsilon_rate, 2)

    return gamma_rate * epsilon_rate
