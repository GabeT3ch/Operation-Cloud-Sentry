class Solution():
    def licenseKeyFormatting(self , s ,  k):
        #clean  by removing all dashes and make everything upper case 
        s = s.replace("-","").upper()
        
        #reverse so the string can be grouped form the left instead of the right
        s = s[::-1]
        
        #build the result from left sort and cleaning
        result = ""
        for i, char in enumerate(s):
            if i > 0 and i % k ==0:
                result += "-"
            result += char

        return result[::-1]
    
    
solution = Solution()
print(solution.licenseKeyFormatting("5F3Z-2e-9-w", 4))    
print(solution.licenseKeyFormatting("2-5g-3-J", 2)) 
     
        