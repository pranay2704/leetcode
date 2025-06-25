
class Solution {
  public:
    bool isBalanced(string& k) {
        // code her
        vector<char> p;
        // p.push_back('(');
        for(int i=0;i<k.size();i++){
            if(k[i]==')'){
                if(p.size()!=0 && p.back()=='(')
                    p.erase(p.end()-1);
                else
                    return false;
            }
            if(p.size()!=0 && k[i]=='}'){
                if(p.back()=='{')
                    p.erase(p.end()-1);
                else
                    return false;
            }
            if(p.size()!=0 && k[i]==']'){
                if(p.back()=='[')
                    p.erase(p.end()-1);
                else
                    return false;
            }
            if(k[i]=='[' || k[i]=='{' || k[i]=='(')
                p.push_back(k[i]);
        }
        if(p.size()==0)
            return true;
        else 
            false;
    }
};
