class Solution():
    def reverseWords(self,s):
        words=s.split()                         #here we use the built in .split() function to split the param / passed in string 's' so it breaks the string down into a list where each word is split ie  ---> ['the', 'sky', 'is', 'blue']
        reversed_words = words[::-1]            # Reverse the ORDER of the words (not the characters).
                                                # [::-1] on a LIST flips element order while keeping each word intact.
                                                # ['the','sky','is','blue'] -> ['blue','is','sky','the']
        return " ".join(reversed_words)         # With the .join() function combine the string s which is in array format by work and glue it back into a string . The " " is for single spaces in between the words onced joined 




solution = Solution()
print(solution.reverseWords("the sky is blue")) #the output is "lue is sky the"