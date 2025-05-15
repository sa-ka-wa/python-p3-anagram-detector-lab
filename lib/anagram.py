# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, candidates):
        """
        This method takes a list of candidate words and returns a list of words that are anagrams of the original word.
        """
        # Sort the letters of the original word
        sorted_word = sorted(self.word)
        # Initialize an empty list to store the anagrams
        anagrams = []
        # Iterate through each candidate word
        for candidate in candidates:
            # Sort the letters of the candidate word
            sorted_candidate = sorted(candidate)
            # If the sorted letters match, it's an anagram
            if sorted_word == sorted_candidate:
                anagrams.append(candidate)
        return anagrams




