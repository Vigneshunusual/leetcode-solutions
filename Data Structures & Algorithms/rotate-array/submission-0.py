class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n

        #reverse full array   nums=[7,6,5,4,3,2,1]
        l=0
        r=n-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

        #reverse first k elements  nums=[5,6,7,4,3,2,1]

        l=0
        r=k-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

        #reverse remaining elements  nums=[5,6,7,1,2,3,4]

        l=k
        r=n-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1


        