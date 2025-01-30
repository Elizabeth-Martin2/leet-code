class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Use sliding window
        vowels = {'a', 'e', 'i', 'o', 'u'}  # Set provides O(1) lookup
        max_vowels = 0

        for letter in s[0:k]:               # O(k)
            if letter in vowels:
                max_vowels += 1

        current_vowels = max_vowels

        for i in range(k, len(s)):          # O(n) where n = len(s)
            # window = [i, i + k]

            if s[i - k] in vowels:
                current_vowels -= 1
            if s[i] in vowels:
                current_vowels += 1

            max_vowels = max(max_vowels, current_vowels)

        return max_vowels