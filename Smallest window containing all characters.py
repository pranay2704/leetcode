class Solution:
    def smallestWindow(self, s, p):
        # code here
        p_sort=''.join(sorted(p))
        for i in range(len(p),len(s)):
            for j in range(len(s)-i):
                sub_s = s[j:j+i]
                sub_s_sort=''.join(sorted(sub_s))
                # print(p_sort,"-",sub_s,"-",sub_s_sort,"-")
                if sub_s_sort.find(p_sort)!=-1:
                    return sub_s
                
        return ''
