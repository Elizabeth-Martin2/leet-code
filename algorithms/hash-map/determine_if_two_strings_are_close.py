class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Base case
        if len(word1) != len(word2):
            # print("False (length)")
            return False
        
        word1_letters = {}
        word2_letters = {}
        for letter in word1:
            if letter not in word1_letters:
                word1_letters[letter] = 0
            word1_letters[letter] += 1

        for letter in word2:
            if letter not in word2_letters:
                word2_letters[letter] = 0
            word2_letters[letter] += 1

        
        # print(f"set(word1_letters.keys()): {set(word1_letters.keys())} ; sorted(word1_letters.values()): {sorted(word1_letters.values())}")
        # print(f"set(word2_letters.keys()): {set(word2_letters.keys())} ; sorted(word2_letters.values()): {sorted(word2_letters.values())}")

        if set(word1_letters.keys()) != set(word2_letters.keys()):
            return False

        if sorted(word1_letters.values()) != sorted(word2_letters.values()):
            return False


        return True


# Observations:
# 1. words must be the same length