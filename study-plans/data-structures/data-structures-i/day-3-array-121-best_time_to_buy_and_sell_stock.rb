# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
  return 0 if prices.size < 2
  
  # sliding window technique
  profit_amount = 0
  start_idx = 0
  end_idx = 1
  
  while end_idx < prices.size
    if prices[start_idx] < prices[end_idx]
      profit_amount = [profit_amount, prices[end_idx] - prices[start_idx]].max
    else
      start_idx = end_idx
    end
    end_idx += 1
  end
  
  profit_amount
end
