class Solution:
    """Finds the union of two sorted arrays"""
    
    # Analysis time: O(n + m) where n = len(a) and m = len(b) 
    # Analysis space: O(n + m) 
    def find_union(self, a: list[int], b: list[int]) -> list:
        """Returns a list containing the union of two sorted arrays"""
        union_dict = {}
        a_ptr = b_ptr = 0
        
        while a_ptr < len(a) and b_ptr < len(b): 
            if a[a_ptr] < b[b_ptr]:
                if a[a_ptr] not in union_dict:
                    union_dict[a[a_ptr]] = 1
                a_ptr += 1
            else:
                if b[b_ptr] not in union_dict:
                    union_dict[b[b_ptr]] = 1
                b_ptr += 1
        
        while a_ptr < len(a):
            if a[a_ptr] not in union_dict:
                union_dict[a[a_ptr]] = 1
            a_ptr += 1
        
        while b_ptr < len(b):
            if b[b_ptr] not in union_dict:
                union_dict[b[b_ptr]] = 1
            b_ptr += 1
        
        return list(union_dict.keys())