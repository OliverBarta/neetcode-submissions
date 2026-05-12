class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            product = 1
            for ii in range(len(nums)):
                if i == ii:
                    continue
                product *= nums[ii]
            out.append(product)

        return out