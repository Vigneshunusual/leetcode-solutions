class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for num in range(n+1):
            b=bin(num)[2:]
            count=0

            for ch in b:
                if ch =='1':
                    count+=1
            ans.append(count)
        return ans
        