'''

Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.
You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
Return the maximum profit you can make.
'''

'''
Need O(N) time
keep three things signal, sell and buy

loop through the array:
 #####be super careful about the update order

        if current price >sell and current price > sell+buy:
        update sell
        
        if buy>sell+fee:
           start to look forward and see if we have another drop back of price with p+fee<buy
        
        if current price <buy:
           update buy
'''




class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        
        

        max_p = 0
        buy = float("inf")
        sell = 0
        
        for i, p in enumerate(prices):
            
            
            if p>sell and p>buy+fee:
                sell = p
                
            if (buy<sell-fee and (p<sell-fee or i == len(prices)-1) ):
                #print "execute", buy, sell
                max_p += sell-buy-fee
                buy = p
                sell = 0
                    
            if p<buy:
                buy = p
                
        return max_p
            
                    
                                                                                                                                                                                                    
