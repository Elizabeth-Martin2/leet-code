class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) >= len(word2):
            longer_word = word1
            shorter_word = word2
        else:
            longer_word = word2
            shorter_word = word1

        # print(f"Shorter word is: {shorter_word}")
        # print(f"Longer word is: {longer_word}")

        merged_str = []
        i = 0
        while i < len(word1) and i < len(word2):
            # print(f"word1[i]: {word1[i]}; word2[i]: {word2[i]}")
            merged_str.append(word1[i])
            merged_str.append(word2[i])
            i += 1

        if len(longer_word) != len(shorter_word):
            merged_str.append(longer_word[i:])

        # print(merged_str)
        return "".join(merged_str)