import unittest
import calculator
import xmlrunner

class TestCalc(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(calculator.mul(5,6), 30)

print calculator.mul(5,6)
if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
