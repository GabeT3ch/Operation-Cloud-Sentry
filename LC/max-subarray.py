class Solution():
    def maxSubArray(self , nums):
        
         #set max and current to 1st position in the array 
        max_sum = nums[0]
        current = nums[0]
        #loop through list  once and check everything from index 1 and on
        for num in nums[1:]:
            current = max(num, current + num)   #decide to either extend or restart
            max_sum = max(max_sum, current)     #keep track of the best sum
        
        return max_sum # return the answer post loop
    
    
    
solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(solution.maxSubArray([1])) 
print(solution.maxSubArray([5,4,-1,7,8]))         
            