import unittest
from word_finder import WordFinder

class TestWordFinder(unittest.TestCase):
    def setUp(self):
        self.wf = WordFinder("/path/to/words.txt")

    def test_random(self):
        word = self.wf.random()
        self.assertIn(word, self.wf.words)

if __name__ == "__main__":
    unittest.main()
