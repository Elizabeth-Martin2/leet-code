class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Base cases numRows == 1 or 2
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        
        pt_list = [[1], [1,1]]
        
        for level in range(2, numRows):
            # Starting at level 2 (really 3) 
            current_level = [1]
            last_level = pt_list[level - 1]
            
            for i in range(0, (level - 1)):
                current_level.append((last_level[i] + last_level[i+1]))
            
            current_level.append(1)
            pt_list.append(current_level)

        return pt_list
