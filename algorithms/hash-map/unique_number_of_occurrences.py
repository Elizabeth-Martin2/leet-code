class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = {}
        for num in arr:
            if num in occ:
                occ[num] += 1
            else:
                occ[num] = 1

        counts = set()
        for key in occ.keys():
            count = occ[key]
            if count in counts:
                return False
            else:
                counts.add(count)
                
        return True