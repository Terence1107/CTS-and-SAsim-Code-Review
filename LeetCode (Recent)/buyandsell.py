def maxProfit(prices):
    '''
    Notes and initial thoughts: 
    use 2 pointers to traverse the list, at 0 and 1
    evaluate the numbers as we traverse
    if the right pointer is greater than the left pointer, calculate the profit
    if the profit is greater than the max profit, update the max profit
    '''

    max_profit = 0
    l,r = 0, 1

    while r <= len(prices) - 1:
        if prices[r] > prices[l]:
            profit = prices[r] - prices[l]
            if max_profit < profit:
                max_profit = profit
        else:
            l = r

        r += 1

        return max_profit




prices = [5,1,5,6,7,1,10]