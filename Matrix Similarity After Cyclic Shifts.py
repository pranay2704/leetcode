class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        col = len(mat[0])
        mat_orig = mat.copy()
        k=k%col
        if k==0:
            return True
        for i in range(len(mat)):
            if i%2==1:
                mat[i] = mat[i][-1:-k-1:-1][::-1] + mat[i][:-k]
            else:
                mat[i] = mat[i][k:] + mat[i][:k]

        print(mat)
        if mat == mat_orig:
            return True
        return False
