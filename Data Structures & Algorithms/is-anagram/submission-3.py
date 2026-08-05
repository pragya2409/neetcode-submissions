class Solution:
    def isAnagram(self, s,t):
        if len(s)!= len(t):
            return False 
        freq_dict= dict()
        for ch in s:
            if ch in freq_dict:
                freq_dict[ch] += 1
            else:
                freq_dict[ch] =1 
        for ch in t:
            if ch not in freq_dict:
                return False
            freq_dict[ch] -= 1

            if freq_dict[ch]< 0:
                return False
        return True
