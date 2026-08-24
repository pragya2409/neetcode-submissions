class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        com_pre= strs[0]
        for word in range (1,len(strs)):
            temp= ""
            for char in range(min(len(com_pre),len(strs[word]))):
                if com_pre[char]== strs[word][char]:
                    temp = temp+com_pre[char]
                else:
                    break 
            com_pre=temp
        return(com_pre)
         
        