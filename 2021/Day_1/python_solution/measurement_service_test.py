import unittest
import measurement_service as ms

# un array del abecedario en mayusculas


class MeasurementServiceTest(unittest.TestCase):

    measures = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def test_correct_result(self):
        result = ms.get_number_magnifications_measurements(self.measures)
        self.assertEqual(result, 7)

    def test_correct_result_three_measurement(self):
        
        for measure in self.measures:
            



        


        


if __name__ == '__main__':
    unittest.main()
