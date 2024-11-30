import unittest 
from REDONEwordfinder import WordFinder
from REDONEspecial_wordfinder import SpecialWordFinder

class TestWordFinder(unittest.TestCase):
    def setUp(self):
        self.wf = WordFinder("words.txt")

    def test_random(self):
        word = self.wf.random()
        self.assertIn(word, self.wf.words)

class TestSpecialWordFinder(unittest.TestCase):
    def setUp(self):
        self.swf = SpecialWordFinder("words.txt")

    def test_random(self):
        word = self.swf.random()
        self.assertIn(word, self.swf.words)

    def test_excludes_comments_and_blanks(self):
        for word in self.swf.words:
            self.assertNotEqual(word, "")
            self.assertFalse(word.startswith("#"))

if __name__ == "__main__":
    unittest.main()