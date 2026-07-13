class Solution():
    def isPalindrome(self, s):
        cleaned_str = '' #create the clean version of the string
        for char in s:    #loop through the original string 
            if char.isalnum(): #check if the char in the str are  a letter or number spaces punctuation or symbols return false 
                cleaned_str += char.lower()   #if true we keep the char but make it lower case so A and a are treated the same
                
        return cleaned_str ==cleaned_str[::-1]  # cleaned_str[::-1] creates a NEW string that is cleaned_str reversed. If reading it backwards gives the exact same string as forwards, it's a palindrome -> True. Otherwise -> False.
            
            
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama")) # Test case 1 True
print(solution.isPalindrome("race a car"))   # Tests case 2 False