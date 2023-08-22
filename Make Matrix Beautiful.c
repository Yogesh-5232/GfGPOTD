class Solution
{
    public:
    //Function to find minimum number of operations that are required 
    //to make the matrix beautiful.
    int findMinOpeartion(vector<vector<int> > matrix, int n)
    {
        int rows=matrix.size();
        int cols=matrix[0].size();
        int maxi=0;
        vector<int> allrowsums;
        for(int i=0;i<n;i++){
            int sum=0;
            int sum1=0;
            for(int j=0;j<n;j++){
                sum+=matrix[i][j];
                sum1+=matrix[j][i];
            }
            allrowsums.push_back(sum);
            maxi=max(maxi,max(sum,sum1));
        }
        
        int result=0;
        for(int i=0;i<n;i++){
            result+=(maxi-allrowsums[i]);
        }
        return result;
    } 
};
