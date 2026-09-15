class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        boat=0
        p.sort()
        l, h = 0, len(p)-1
        while l <= h:
            if p[l] + p[h]<= limit:
                l+=1
            h-=1 
            boat +=1
        return boat

        