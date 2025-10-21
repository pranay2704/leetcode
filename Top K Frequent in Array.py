class Solution:
    def topKFreq(self, arr, k):
        count1 = [[] for _ in range(len(arr) + 1)]  # to store elements by frequency
        count = {}

        # Step 1: Count frequency of each element
        for i in arr:
            if i in count:class Solution:
    def topKFreq(self, arr, k):
        count1 = [[] for _ in range(len(arr) + 1)]  # to store elements by frequency
        count = {}

        # Step 1: Count frequency of each element
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        # Step 2: Group numbers based on their frequencies
        for num, freq in count.items():
            count1[freq].append(num)

        res = []
        # Step 3: Collect top k frequent elements (start from highest frequency)
        for freq in range(len(count1) - 1, 0, -1):
            # count1[freq].sort(reverse=True)
            # print(count1[freq])
            for num in sorted(count1[freq],reverse=True):
                res.append(num)
                if len(res) == k:
                    return res
        return res

                count[i] += 1
            else:
                count[i] = 1

        # Step 2: Group numbers based on their frequencies
        for num, freq in count.items():
            count1[freq].append(num)

        res = []
        # Step 3: Collect top k frequent elements (start from highest frequency)
        for freq in range(len(count1) - 1, 0, -1):
            # count1[freq].sort(reverse=True)
            # print(count1[freq])
            for num in sorted(count1[freq],reverse=True):
                res.append(num)
                if len(res) == k:
                    return res
        return res
