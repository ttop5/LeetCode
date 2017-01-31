/**
 * @param {number[]} prices
 * @return {number}
 */
function maxProfit(prices) {
  if(prices.length === 0) {
    return 0;
  }
  let low = prices[0];
  let profit = 0;
  for (let i=1; i<(prices.length); i++) {
    if(prices[i]<low) {
      low = prices[i];
    }else if((prices[i] - low) > profit){
      profit = prices[i] - low;
    }
  }
  return profit;
}
