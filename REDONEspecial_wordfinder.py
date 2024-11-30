import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filepath):
        self.words = self.read_words_from_file(filepath)
        print(f"{len(self.words)} words read")

    def read_words_from_file(self, filepath):
        with open(filepath, 'r') as file:
            words = file.readlines()
            return [words.strip() for word in words] # Remove newline characters

    def random(self):
        return random.choice(self.words)

    def __repr__(self):
        return f"<WordFinder words={lens(self.words)}>"


class SpecialWordFinder(WordFinder):
    """Special Word Finder: excludes blank lines and comments."""

    def read_words_from_file(self, filepath):
        with open(filepath, 'r') as file:
            words = file.readlines()
            #Filter out blank lines and comments
            return [word.strip() for word in words if word.strip() and not word.startswith('#')]

        def __repr__(self):
            return f"<SpecialWordFinder words = {len(self.words)}>"