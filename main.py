class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter as ct
        return [k for (k,v) in ct(nums).most_common(k)] 
    
sol = Solution()

nums = [1, 1, 1, 2, 2, 3]
k=2

print(sol.topKFrequent(nums, k))