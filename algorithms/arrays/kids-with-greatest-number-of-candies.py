class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        max_candies = max(candies)

        for i, candy in enumerate(candies):
            if candy + extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)

        return res