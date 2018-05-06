# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# Example:

# Input: 4
# Output: [
# [".Q..",  // Solution 1
#  "...Q",
#  "Q...",
#  "..Q."],
#
# ["..Q.",  // Solution 2
#  "Q...",
#  "...Q",
#  ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        for j in range(n):
            extend([j], n, ans)
        return ans


def convert(sofar, n):
    board = []
    for j in sofar:
        temp = '.'*n
        board.append(temp[:j] + 'Q' + temp[j+1:])
    return board
    
def extend(sofar, n, ans):
    if len(sofar) == n:
        ans.append(convert(sofar, n))
        return
    
    for j in range(n): 
        if j in sofar:
            continue
        if valid(sofar, j):
            extend(sofar+[j], n, ans)
    

def valid(sofar, j):
    for i in range(len(sofar)):
        delta = len(sofar) - i
        if sofar[i]-j == delta or j-sofar[i] == delta:
            return False
    return True
        
