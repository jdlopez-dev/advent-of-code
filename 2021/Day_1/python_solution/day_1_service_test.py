import unittest
import day_1_service as ms

# un array del abecedario en mayusculas


class MeasurementServiceTest(unittest.TestCase):

    measures = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    def test_correct_result(self):
        result = ms.get_number_magnifications_measurements(self.measures)
        self.assertEqual(result, 7)

    def test_correct_result_three_measurement(self):
        result = ms.get_number_magnifications_three_measurements(self.measures)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
