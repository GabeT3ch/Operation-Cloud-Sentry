class Solution():
    def containsDuplicate(self , nums):
        seen = set() #we sue a set because they do not contain duplicates which is what we are looking for 
        for number in nums:
            if number in seen:
                return True
            seen.add(number) # if the number is in see we add it to the empty set above and thats what is checked when its time to return True or False
            
        return False
    



solution = Solution()
print(solution.containsDuplicate([1,2,3,4,5,3]))
print(solution.containsDuplicate([1,2,3,4,5]))