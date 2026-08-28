class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        buy,sell = 0,1
        cheapest = prices[buy]
        maxProf = 0
        while True:
            value = prices[sell]-prices[buy]
            maxProf = max(maxProf,value)
            if(prices[sell]<cheapest):
                buy = sell
                cheapest = prices[buy]
                print("new cheapest: ",cheapest)
            sell+=1
            if(sell>=len(prices)):
                return maxProf
            
