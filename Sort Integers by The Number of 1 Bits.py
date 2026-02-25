    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        def check(a):
            return bin(a)[2:].count('1')
        arr.sort(key=check)
        print(arr)
        return arr
