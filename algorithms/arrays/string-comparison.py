class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0

        while j < len(chars):
            char = chars[j]
            counter = 0

            while j < len(chars) and chars[j] == char:
                j += 1
                counter += 1

            chars[i] = char
            i += 1
            if counter > 1:
                for digit in str(counter):
                    chars[i] = digit
                    i += 1

        return i