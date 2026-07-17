from collections import Counter


class Solution():
    
    def canConstruct(self , ransomNote , magazine):
        magazine_count = Counter(magazine)
        ransom_count = Counter(ransomNote)
        
        for char in ransom_count:
            if magazine_count[char] <  ransom_count[char]:
        
                return False
            
        return True
            
            
solution = Solution()
print(solution.canConstruct('aa','aab'))
print(solution.canConstruct('aa','ab'))
print(solution.canConstruct('aa','aab'))
        