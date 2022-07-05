import unittest
from API import find_song


class TestFileName(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(find_song("Meet me in The garden"), "Dent May")
        self.assertEqual(find_song("All TOO well"), "Taylor Swift")
        self.assertEqual(find_song("It's called: freefall"), "Rainbow Kitten Surprise")

    def test_weird(self):
        self.assertEqual(find_song("hsuianoehaobc"), "Unknown")
        self.assertEqual(find_song(""), "Unknown")
        self.assertEqual(find_song(" "), "Unknown")


if __name__ == '__main__':
    unittest.main()