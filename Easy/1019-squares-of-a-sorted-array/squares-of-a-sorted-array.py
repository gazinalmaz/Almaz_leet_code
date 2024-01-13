class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_new = []
        left = 0
        right = len(nums) - 1
        while left <= right:
            if ((nums[left])**2) < ((nums[right])**2):
                nums_new.append((nums[right])**2)
                right -= 1
            else:
                nums_new.append((nums[left])**2)
                left += 1
        return reversed(nums_new)
        
        
        
        
        
        
        
        
        
        
        
        
        
        # new_nums = []
        # for num in nums:
        #     new_nums.append(num*num)
        # new_nums.sort()
        # return new_nums    