import unittest
from serial_generator import SerialGenerator

class TestSerialGenerator(unittest.TestCase):
    def setUp(self):
        self.serial = SerialGenerator(start=100)

    def test_generate(self):
        self.assertEqual(self.serial.generate(), 100)
        self.assertEqual(self.serial.generate(), 101)
        self.assertEqual(self.serial.generate(), 102)

    def test_reset(self):
        self.serial.generate()
        self.serial.generate()
        self.serial.reset()
        self.assertEqual(self.serial.generate(), 100)

if __name__ == "__main__":
    unittest.main()
