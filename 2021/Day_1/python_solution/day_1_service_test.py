import unittest
import day_1_service as ms

# un array del abecedario en mayusculas


class Day1ServiceTest(unittest.TestCase):

    measures = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    positions = ["forward 5", "down 5",
                 "forward 8", "up 3", "down 8", "forward 2"]

    def test_correct_result(self):
        result = ms.get_number_magnifications_measurements(self.measures)
        self.assertEqual(result, 7)

    def test_correct_result_three_measurement(self):
        result = ms.get_number_magnifications_three_measurements(self.measures)
        self.assertEqual(result, 5)

    def test_final_position(self):

        final_result = ms.get_final_position(self.positions)

        self.assertEqual(final_result, 150)


if __name__ == '__main__':
    unittest.main()
