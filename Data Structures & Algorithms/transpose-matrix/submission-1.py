class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res=[]
        n=len(matrix)
        m=len(matrix[0])
        for j in range(m):  #j=0,1,
            row=[]
            for i in range(n):   #i=0,1
                row.append(matrix[i][j])
            res.append(row)
        return res
        