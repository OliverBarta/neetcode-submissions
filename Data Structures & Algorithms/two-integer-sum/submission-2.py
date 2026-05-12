class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        for idxa in range(len(nums)):
            for idxb in range(len(nums)-idxa-1):
                if nums[idxa] + nums[idxb+idxa+1] == target:
                    return [idxa, idxb+idxa+1]