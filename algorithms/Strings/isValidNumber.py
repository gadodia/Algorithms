
class Solution:
    
    def convertToNumber(self, string):
        if not string:
            return False
        # if not string[0].isdigit() and string[0] != '-' and string[0] != '.':            
        #     return False
        foundDecimal = False
        foundSign = False
        if string[0] == '-':
            string = string[1:]
        for i, char in enumerate(string):             
            if char  == '.':
                if foundDecimal:
                    return False
                else:
                    foundDecimal = True
                    if i == len(string)-1:
                        return False
            elif char == 'e':
                if foundSign:
                    return False
                else:
                    foundSign = True
                    if i == len(string)-1:
                        return False
            elif not char.isdigit():
                return False            
        return True
        

print(Solution().convertToNumber("123456"))
print(Solution().convertToNumber(""))
print(Solution().convertToNumber("123456.12345"))
print(Solution().convertToNumber("-."))
print(Solution().convertToNumber("1e10"))
print(Solution().convertToNumber("1.23e4"))
