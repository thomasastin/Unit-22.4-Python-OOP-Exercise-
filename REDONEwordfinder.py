import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filepath):
        self.words = self.read_words_from_file(filepath)
        print(f"{len(self.words)} words read")

    def read_words_from_file(self, filepath):
        with open(filepath, 'r') as file:
            words = file.readlines()
            return [word.strip() for word in words] #Remove newline characters 

    def random(self):
        return random.choice(self.words)

