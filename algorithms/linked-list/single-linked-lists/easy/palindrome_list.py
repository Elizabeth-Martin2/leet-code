class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = [head.val]
        node = head
        
        while node and node.next:
            node = node.next
            if node:
                temp.append(node.val)
        

        left, right = 0, len(temp) - 1
        
        while left < right:
            if temp[left] != temp[right]:
                return False
            left += 1
            right -= 1

        return True
    
    
    def isPalindromeBF(self, head: Optional[ListNode]) -> bool:
        temp = [str(head.val)]
        node = head
        
        while node and node.next:
            node = node.next
            if node:
                temp.append(str(node.val))
        
        temp = ''.join(temp)
        
        return temp == temp[::-1]
    
