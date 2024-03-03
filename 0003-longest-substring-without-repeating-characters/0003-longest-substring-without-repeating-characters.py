class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        start_pointer = 0 
        end_pointer = 0 
        maximum_length = float("-inf")
        frequency = [0] * 256

        while end_pointer < len(s):
            element_to_add = s[end_pointer]
            if frequency[ord(element_to_add)] == 0:
                frequency[ord(element_to_add)] += 1 
                end_pointer += 1 
            else:
                character_to_remove = s[start_pointer]
                frequency[ord(character_to_remove)] -= 1 
                start_pointer += 1 

            
            maximum_length = max(maximum_length, end_pointer - start_pointer)
        
        return maximum_length
            


            
        