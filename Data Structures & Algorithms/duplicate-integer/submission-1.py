class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        idx = 0
        
        for num in nums:
            if idx == len(nums)-1:
                continue
            if nums[idx+1] == num:
                return True
            idx += 1
        return False