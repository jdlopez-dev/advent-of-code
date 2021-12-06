import unittest
import advent_of_code_service as ms


class AdventOfCodeServiceTest(unittest.TestCase):

    measures = ["199", "200", "208", "210",
                "200", "207", "240", "269", "260", "263"]
    positions = ["forward 5", "down 5",
                 "forward 8", "up 3", "down 8", "forward 2"]

    binary_numbers = ["00100",
                      "11110",
                      "10110",
                      "10111",
                      "10101",
                      "01111",
                      "00111",
                      "11100",
                      "10000",
                      "11001",
                      "00010",
                      "01010"]

    def test_day_one_part_one(self):
        result = ms.get_number_magnifications_measurements(self.measures)
        self.assertEqual(result, 7)

    def test_day_one_part_two(self):
        result = ms.get_number_magnifications_three_measurements(self.measures)
        self.assertEqual(result, 5)

    def test_day_two_part_one(self):
        final_result = ms.get_final_position(self.positions)

        self.assertEqual(final_result, 150)

    def test_day_two_part_two(self):
        final_result = ms.get_final_position_with_aim(self.positions)

        self.assertEqual(final_result, 900)

    def test_day_three_part_one(self):
        power_consumption = ms.get_power_consumption(self.binary_numbers)
        self.assertEqual(power_consumption, 198)


if __name__ == '__main__':
    unittest.main()
