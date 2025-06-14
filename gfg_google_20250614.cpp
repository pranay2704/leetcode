class Solution {
  public:
    int maxSubarraySum(vector<int> &arr) {
        // Your code here
        int total=0;
        int larg=INT_MIN;
        vector<int> sum;
        for(auto i: arr){
            total+=i;
            sum.push_back(total);
            if(total>larg){
                larg=total;
            }
        }
        
        for(int i=0;i<arr.size();i++){
            for(int j=i+1;j<sum.size();j++){
                // cout<<sum[j]<<"-"<<arr[i]<<"-"<<sum[j]-(arr[i])<<"\n";
                if((sum[j]-arr[i])>larg){
                    larg=sum[j]-arr[i];
                }
                sum[j]-=arr[i];
            }
        }
        
        return larg;
    }
};
