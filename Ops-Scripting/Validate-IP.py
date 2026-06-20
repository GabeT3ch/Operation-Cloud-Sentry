class Solution:

    def validateIPAddress(self,queryIP):
        if "." in queryIP:
            return "IPv4" if self.IPv4(queryIP) else "Neither"
        elif ":" in queryIP:
            return "IPv6" if self.IPv6(queryIP) else "Neither"
        else:
            return "Neither"




    def IPv4(self,address):
        parts = address.split(".") #split "192.168.4.1 into ['192','168','4','1']

        if len(parts) !=4: #ipv4 can only have 4  octets.
            return False
        for part in parts:
            if not part: #the octets cannot be empty
                return False
            if not part.isdigit(): #the octets can only be populated with integers
                return False
            if len(part) > 1 and part[0] == '0': #this eliminates leading zeros's
                return False
            if int(part) > 255: #the range for piv4 is 0-255 anything outside of that is invalid
                return False
            
        return True # this returns the string if it survives all these conditions
        
        


    def IPv6(self,address):
        parts= address.split(":") # we split IPv6 with : not .
        if len(parts) != 8: #ipv6 has 8 octets / parts
            return
        for part in parts:
          if not part: #cannot be empty
              return False
          
          if len(part)  > 4: #octet must stillbe 1-4 char
              return False
          
          try: #try except block to handle valid hex format check
              int(part,16)
          except ValueError:
              return False
        
        return True
        



solution = Solution()
print(solution.validateIPAddress("172.16.254.1"))        # should print "IPv4"
print(solution.validateIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))  # should print "IPv6"
print(solution.validateIPAddress("256.256.256.256"))     # should print "Neither"