# Given a string s, partition s such that every substring of the partition is a palindrome.
# 
# Return all possible palindrome partitioning of s.
#
# Example:
# 
# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) < 2:
            return [[s]]
        pal_table = {}
        queue = []
        for i in range(1, len(s)+1): # end index
            for j in range(len(s)-i+1): # index
                if s[j] == s[j-1+i]:
                    if i <= 2:
                        if j not in pal_table:
                            pal_table[j] = set()
                        pal_table[j].add(i)
                        if j == 0:
                            queue.append((j+i, [s[j:j+i]]))
                    elif (j+1 in pal_table) and (i-2 in pal_table[j+1]):
                        pal_table[j].add(i)
                        if j == 0:
                            queue.append((j+i, [s[j:j+i]]))
                       
        ans = []
        while len(queue) > 0:
            sidx, path = queue.pop(0)
            if sidx == len(s):
                ans.append(path)
            if sidx not in pal_table:
                continue
            for length in pal_table[sidx]:
                queue.append((sidx+length, path+[s[sidx: sidx+length]]))
        
        
        return ans      
        
