class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        cust = 0
        maxi = 0
        
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                cust += customers[i]
        
        for i in range(len(grumpy) - minutes + 1):
            extra = 0
            
            for j in range(i, i + minutes):
                if grumpy[j] == 1:
                    extra += customers[j]
            
            maxi = max(maxi, extra)
        
        return cust + maxi