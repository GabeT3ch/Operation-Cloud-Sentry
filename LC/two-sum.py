class Solution:
    def two_sum(self, nums,target):
        hash_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash_map:
                return [hash_map[diff] , i]
            hash_map[n] = i
        
       
    

solution = Solution()
print(solution.two_sum([1,3,15,5,8] , 11) )