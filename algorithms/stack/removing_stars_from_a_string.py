class Solution:
    def removeStars(self, s: str) -> str:
        starless = [s[0]]
        for i in range(1, len(s)):
            if s[i] != "*":
                starless.append(s[i])
            else:
                if starless:
                    starless.pop()
            # print(starless)
        return ''.join(starless)