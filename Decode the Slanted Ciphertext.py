class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        start = 0
        st = ''
        lt = (len(encodedText)//rows)+1
        while start<(lt-1):
            end=start
            st+=encodedText[end]
            for i in range(end+lt,len(encodedText),lt):
                st+=encodedText[i]
            start+=1
        st = st.rstrip()
        return st
