class Solution:
    def reverseWords(self, s: str) -> str:
        no_spaces = s.split()
        # return ' '.join(no_spaces[::-1]) # one-liner solution

        rev_s = []
        for i in range(1, len(no_spaces) + 1):
            rev_s.append(no_spaces[-i])

        # print(rev_s)
        return " ".join(rev_s)
