class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = current_alt = 0
        for alt in gain:
            current_alt += alt
            max_alt = max(max_alt, current_alt)

        return max_alt