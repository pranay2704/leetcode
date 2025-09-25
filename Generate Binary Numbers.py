class Solution:
    def generateBinary(self, n):
        result = []
        for num in range(1, n + 1):
            binary = ""
            temp = num
            while temp > 0:
                binary = str(temp % 2) + binary
                temp //= 2
            result.append(binary)
        return result
