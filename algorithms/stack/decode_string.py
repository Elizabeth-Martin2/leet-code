class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        current_count = ""
        current_string = ""

        for i in range(len(s)):
            if s[i].isdigit():
                current_count += s[i]
            elif s[i] == "[":
                string_stack.append(current_string)
                count_stack.append(current_count)
                current_string = ""
                current_count = ""
            elif s[i] == "]":
                popped_counter = count_stack.pop()
                repeated_string = current_string * int(popped_counter)
                
                last_string = string_stack.pop()
                current_string = last_string + repeated_string
            else: # it's a letter
                current_string += s[i]
        
        return current_string

# Complexity: O(n) where n = len(s)