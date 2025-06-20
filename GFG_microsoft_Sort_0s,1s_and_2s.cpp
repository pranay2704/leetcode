class Solution {
  public:
    void sort012(vector<int>& arr) {
        // code here
        int max=-1;
        for(auto i: arr){
            if(max<i)
                max=i;
        }
        
        
        
        vector<int> temp(3,0);
        for(auto i: arr){
            temp[i]=temp[i]+1;
        }
        int z=arr.size();
        arr.clear();
        int j=0;
        while(temp[max]!=0){
            if(temp[j]){
                arr.push_back(j);
                temp[j]-=1;
            }
            else
                j++;
        }
        
    }
};
