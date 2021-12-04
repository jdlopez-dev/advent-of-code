import advent_of_code_service as service
from advent_of_code_utils import print_day, get_data


data = get_data('input.txt')

day = "One"
part_one = service.get_number_magnifications_measurements(data)
part_two = service.get_number_magnifications_three_measurements(data)
print_day(day, part_one, part_two)

# --------------------------------------------------

data = get_data('input_day_2.txt')

day = "Two"
part_one = service.get_final_position(data)
part_two = service.get_final_position_with_aim(data)
print_day(day, part_one, part_two)
