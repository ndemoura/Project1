import unittest
from API import find_song


class TestFileName(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(find_song("Meet me in The garden"), "Dent May")
        self.assertEqual(find_song("All TOO well"), "Taylor Swift")
        self.assertEqual(find_song("I love you SO"), "The Walters")

    def test_weird(self):
        self.assertEqual(find_song("hsuianoehaobc"), "Unknown")
        self.assertEqual(find_song("Meet meeeee inw The garden"), "Unknown")
        self.assertEqual(find_song(" "), "Unknown")


if __name__ == '__main__':
    unittest.main()