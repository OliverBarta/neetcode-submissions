class Solution {
public:
    int maxArea(vector<int>& heights) {
        int output = 0;

        for (int i = 0; i < heights.size(); i++) {
            for (int j = i + 1; j < heights.size(); j++) {
                // int water = ;
                output = max(output, (j - i) * min(heights[i], heights[j]));
                
            }
        }
        return output;
    }
};
