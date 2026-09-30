class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0 
        seen= set()
        maxlen=0

        while r <= len(s)-1:
            if s[r] not in seen:
                seen.add(s[r])
                maxlen= max(maxlen,(r-l)+1)
                r+=1
            else :
                seen.remove(s[l])
                l+=1
        return maxlen
        