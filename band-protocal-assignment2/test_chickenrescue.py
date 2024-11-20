from chickenrescue import chicken_rescue 
import unittest

class TestBossBabyRevenge(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(chicken_rescue([2, 5, 10, 12, 15], 5), 2)

    def test_case_2(self):
        self.assertEqual(chicken_rescue([1, 11, 30, 34, 35, 37], 10), 4)


if __name__ == '__main__':
    unittest.main()