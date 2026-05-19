class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        res=[]
        for j in range(m):
            rows=[]
            for i in range(n):
                rows.append(matrix[i][j])
            res.append(rows)
        for rows in res:
            l=0
            r=n-1
            while l<r:
                rows[l],rows[r]=rows[r],rows[l]
                l+=1
                r-=1
        for i in range(n):
            matrix[i]=res[i]



        