class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #om

        newanag={}
        for i in range (len(strs)):
            key = ''.join(sorted(strs[i]))

            if key not in newanag:
                newanag[key] = []
        
            newanag[key].append(strs[i])
            
        return list(newanag.values())
        

        
        
                    
                        
        