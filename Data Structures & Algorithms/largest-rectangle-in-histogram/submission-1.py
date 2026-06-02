class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        largest = max(max(heights), len(heights) * min(heights))
        if len(heights) == 1 or len(heights) == 2:
            return largest

        map = {}
        size = 1

        while size <= max(heights):
            map[size] = []
            
            i = 0
            while i < len(heights):
                if heights[i] >= size:
                    map[size].append(i)
                i += 1

            if len(map[size]) <= 1:
                map.pop(size, None)
                break
            
            map[size].sort()
            
            size += 1


        for size in map:
            i = 0
            whichSeq = 0
            seqs = [1]
            while i < len(map[size]) - 1:
                if map[size][i] + 1 == map[size][i + 1]:
                    seqs[whichSeq] += 1
                else:
                    seqs.append(1)
                    whichSeq += 1
                i += 1
            largest = max(largest, size * max(seqs))

        
        return largest

            