# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
# The largest rectangle is shown in the shaded area, which has area = 10 unit.

# Example:

# Input: [2,1,5,6,2,3]
# Output: 10

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        hq = [heights[0]]
        cq = [1]
        ans = heights[0]
        for i in range(1, len(heights)):
            if heights[i] == heights[i-1]:
                cq[-1] += 1
            elif heights[i] < heights[i-1]:  #decrease
                ans = decr(heights, i, hq, cq, ans)
            else:
                hq.append(heights[i])
                cq.append(1)
        ans = summ(hq, cq, ans)
        return ans

        
def decr(heights, i, hq, cq, ans):
    h = heights[i]
    accum = 0
    while len(hq) != 0:
        if hq[-1] > h:
            accum += cq[-1]
            cq.pop()
            ans = max(ans, hq[-1]*accum)
            hq.pop()
        else:
            break
    hq.append(h)
    cq.append(accum+1)
    return ans
            
    
def summ(hq, cq, ans):
    accum = 0
    #while len(hq) != 0:
    #    h, count = hq.pop()
    for i in reversed(range(len(hq))):
        accum += cq[i]
        ans = max(ans, hq[i]*accum)
    return ans
    
    
