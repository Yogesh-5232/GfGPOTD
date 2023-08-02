class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        #code here
        q=[(0,0,0)]
        while q:
            i,j,res=q.pop(0)
            if (i,j)==(X,Y):
                return res
            next1 = ((i+1,j),(i-1,j),(i,j+1),(i,j-1))
            for k,l in next1:
                if 0<=k<N and 0<=l<M and A[k][l]==1:
                    q.append((k,l,res+1))
                    A[k][l]=0
        return -1
