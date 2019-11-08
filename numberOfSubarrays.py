class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # count
        arr = []
        for i, x in enumerate(nums):
            if x % 2 != 0:
                arr.append(i)   
        arr.append(len(nums))
        
        # not satisify
        if len(arr) <= k:
            return 0
        
        # calculate
        count = 0
        count +=  (arr[0] + 1) * (arr[k] - arr[k-1])
        for i in range(k+1, len(arr)):
            count += (arr[i-k] - arr[i-k-1]) * (arr[i] - arr[i-1])
            
        return count 
