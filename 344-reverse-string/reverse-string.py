class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            
            left +=1
            right -=1
           
           
                
                
        
        
        #s.reverse()
        #s[:] = s[::-1]
        #s-new = s[::-1]        The : in the brackets [] indicates slicing.
# The ::-1 specifies the slice operation:
# The first colon : means "start at the beginning and go to the end".
# The -1 specifies the step, in this case, -1, meaning "go backwards one step at a time".
# Therefore, s[::-1] generates a new list that is the reverse of s.
# 

        # def helper(left, right):
        #     if left < right:
        #         s[left], s[right] = s[right], s[left]
        #         helper(left +1, right - 1)
        # helper(0, len(s)-1)   

        
        
        # left, right = 0, len(s) -1 #Set the pointer left at index 0, and the pointer right at index n - 1, 
        #                             #where n is the number of elements in the array.
        # while left <right:
        #     s[left], s[right] = s[right], s[left]
        #     left, right = left+1, right-1
            
            





        