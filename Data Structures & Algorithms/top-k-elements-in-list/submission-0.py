class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        noDuplicate = []

        for x in nums:
            if x in noDuplicate:
                continue
            noDuplicate.append(x)
        
        numInstances = []

        for x in noDuplicate:
            numInstances.append(nums.count(x))

        output = []

        for x in range(k):
            output.append(noDuplicate[numInstances.index(max(numInstances))])
            numInstances[numInstances.index(max(numInstances))] = 0
        
        return output
        