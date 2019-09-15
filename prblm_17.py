# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# 17. Letter Combinations of a Phone Number

class Solution(object):
    
    def __init__(self):
        self.phone_pad = dict()
        self.phone_pad[2] = ('a','b','c')
        self.phone_pad[3] = ('d','e','f')
        self.phone_pad[4] = ('g','h','i')
        self.phone_pad[5] = ('j','k','l')
        self.phone_pad[6] = ('m','n','o')
        self.phone_pad[7] = ('p','q','r','s')
        self.phone_pad[8] = ('t','u','v')
        self.phone_pad[9] = ('w','x','y','z')
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: # return [] if no digits in input
            return []
        if len(digits) == 1: # return all characters for a single digit input
            return list(self.phone_pad[int(digits)])
        result = self.letterCombinations(digits[1:]) # recursion if more than a single digit in the input
        
        temp_result = []
        
        for word in result: # concatenate left most key characters with all possible combination of characters from recursive output
            for key in self.phone_pad[int(digits[0])]:
                temp_result.append(key+word)
                
        return temp_result # return result with all possible combination of characters
        
        
