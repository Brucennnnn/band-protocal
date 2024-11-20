from bossbabyrevenge import boss_baby_revenge

import unittest

class TestBossBabyRevenge(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(boss_baby_revenge(""), "Good boy")

    def test_starts_with_R(self):
        self.assertEqual(boss_baby_revenge("R"), "Bad boy")
        self.assertEqual(boss_baby_revenge("RSSRR"), "Bad boy")

    def test_good_boy(self):
        self.assertEqual(boss_baby_revenge("SRSSRRR"), "Good boy")
        self.assertEqual(boss_baby_revenge("SSRSRR"), "Good boy")

    def test_bad_boy(self):
        self.assertEqual(boss_baby_revenge("SRRSSR"), "Bad boy")
        self.assertEqual(boss_baby_revenge("SSSRRRRS "), "Bad boy")

if __name__ == '__main__':
    unittest.main()