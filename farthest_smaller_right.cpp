class Solution {
  public:
    vector<int> farMin(vector<int>& arr) {
        // code here
        vector<int> res;
        for( int i =0;i<arr.size();i++){
            
            int j=arr.size()-1;
            while(j>=0 && j>i && arr[i]<=arr[j]){
                j--;
            }
            if(i==j)
                res.push_back(-1);
            else 
                res.push_back(j);
        }
        return res;
    }
};
