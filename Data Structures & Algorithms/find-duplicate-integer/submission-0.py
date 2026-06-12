class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count={}
        for ch in nums:

            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
            
        for key in count:
            if count[key]>1:
                return key
        