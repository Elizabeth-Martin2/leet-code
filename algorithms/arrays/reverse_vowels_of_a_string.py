class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"A", "E", "I", "O", "U"}
        s_list = list(s)

        first_ptr = 0
        last_ptr = len(s) - 1

        while first_ptr < last_ptr:
            if s_list[first_ptr].upper() in vowels and s_list[last_ptr].upper() in vowels:
                s_list[first_ptr], s_list[last_ptr] = s_list[last_ptr], s_list[first_ptr]
                first_ptr += 1
                last_ptr -= 1

            if s_list[first_ptr].upper() not in vowels:
                first_ptr += 1

            if s_list[last_ptr].upper() not in vowels:
                last_ptr -= 1

        return "".join(s_list)
