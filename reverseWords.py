# Given an input string , reverse the string word by word. 

# Example:

# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# Note: 

# A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces.
# The words are always separated by a single space.

class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        reverse(str, 0, len(str)-1)
        j = 0
        for i in range(len(str)):
            if str[i] == ' ':
                reverse(str, j, i-1)
                j = i+1
        reverse(str, j, len(str)-1)
        
        

def reverse(str, start, end):
    str[start:end+1] = reversed(str[start:end+1])
    
    
                
                
                
