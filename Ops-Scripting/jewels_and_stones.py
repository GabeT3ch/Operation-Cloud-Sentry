class Solution():
    def numJewelsInStones(self , jewels , stones):
        jewel_set = set(jewels)
        count = 0
        
        for stone in stones:
            if stone in jewel_set:
                count += 1
                
            
            
            
        return count
    
    
solution = Solution()
print(solution.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(solution.numJewelsInStones(jewels = "z", stones = "ZZ"))