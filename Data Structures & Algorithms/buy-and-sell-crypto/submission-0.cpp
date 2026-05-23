class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int output = 0;

        for (int buy = 0; buy < prices.size() - 1; buy++) {
            for (int sell = buy + 1; sell < prices.size(); sell++) {
                if (prices[sell] - prices[buy] > output) {
                    output = prices[sell] - prices[buy];
                }
            }
        }
        return output;
    }
};
