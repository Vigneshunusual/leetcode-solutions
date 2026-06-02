class Solution:
    def hammingWeight(self, n: int) -> int:
        b=bin(n)
        count=0
        for ch in b:
            if ch == '1':
                count+=1
        return count
        