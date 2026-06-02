class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)
        m = int(r/2)
        
        while nums[m] != target and abs(r - l) > 1:
            
            if nums[m] > target:
                r = m
            else:
                l = m
            
            m =int((l+r)/2)
        
        if nums[m] == target:
            return m
        else:
            return -1