def main():
    def rec(arr, i):  # FIXED: removed 'self' parameter
        if i == 0:
            return [[]]
        if not arr:
            return []
        
        # WITH first element: prepend arr[0] to combinations of size i-1 from rest
        res1 = rec(arr[1:], i-1)
        with_first = [[arr[0]] + j for j in res1]
        
        # WITHOUT first element: combinations of size i from rest  
        without_first = rec(arr[1:], i)
        
        return with_first + without_first  # FIXED: combine BOTH cases
    
    arr1 = rec([1,2,3,4,5,6,7], 3)
    print(f"Total: {len(arr1)} combinations")  # 35
    for combo in arr1:
        print(combo)

main()
