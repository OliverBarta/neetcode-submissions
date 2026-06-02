class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        k = math.ceil(sum(piles)/h)

        extraHours = h-len(piles)

        piles.sort(reverse=True)

        print(piles, " | ", extraHours)
        if extraHours < len(piles):
            k = max(math.ceil(piles[0]/(extraHours+1)), piles[extraHours])
        else:
            k = max(math.ceil(piles[0]/(extraHours+1)),math.ceil(sum(piles)/h))
        
        return k