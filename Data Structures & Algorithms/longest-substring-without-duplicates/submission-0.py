class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        l, r = 0, 0 
        maxlen=0
        while r<=len(s)-1:
            if s[r] not in seen:
                seen.add(s[r])
                maxlen= max(maxlen, (r-l)+1)
                r+=1
            else:
                seen.discard(s[l])
                l+=1
        return maxlen 

