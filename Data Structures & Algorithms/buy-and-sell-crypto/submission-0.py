class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        daytobuy=prices[0]
        maxprofit=0
        for cost in prices:
            if cost<daytobuy:
                daytobuy=cost
            curprofit= cost-daytobuy
            if curprofit>maxprofit:
                maxprofit=curprofit
        return maxprofit