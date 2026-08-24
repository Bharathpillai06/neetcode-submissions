class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """num = 0
        for i in range(len(arr)-k+1):
            if sum(arr[i:i+k])//k >= threshold:
                num +=1
        return num"""

        num = 0
        window = sum(arr[:k])

        if window // k >= threshold:
            num += 1

        for i in range(k, len(arr)):
            window += arr[i]
            window -= arr[i-k]

            if window // k >= threshold:
                num += 1

        return num