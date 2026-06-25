class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # checks the len because anagrams have the same len the chars are just in a different order
            return False
        dict = {}              # using a dictionary to efficiently map char to how many times the appear
        for char in s: #count up from s
            if char in dict:
                dict[char] += 1 # if the char has been seen before add one
            else:
                dict[char] = 1 #if this is the 1st time the char is seen start the count at 1 


        for char in t: #count down from t "spending" one of each letter from the tally
            if char in dict:
                dict[char] -=1
            else: 
                return False # If t has a letter that s never had, it's not in counts not an anagram.
        
        # If t used the exact same letters in the exact same amounts,
        # every count is now 0. Any leftover (non-zero) means a mismatch. 
        # this will verify s and t are balaneced
        for count in dict.values(): 
            if count !=0:
                return False

        return True #conditions passed and it is indeed an anagram



solution = Solution()
print(solution.isAnagram('rat','tar'))